from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Comment, Post, PostCategory
from .forms import CommentForm, PostForm, UpdateForm # import form classes.
#from django.contrib.auth.mixins import LoginRequiredMixin


#def home(request):
 #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    
    # Using queryset argument.
    # An alternative to using the 'model' argument.
    #queryset = Post.objects.all()#.order_by('author').distinct('author')
    template_name = 'home.html'
    context_object_name = 'post_list'
    #paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        category_menu = PostCategory.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

    # def get_queryset(self):
    #     self.post = get_object_or_404(Post, author=self.kwargs['self.pk'])
    #     return Post.objects.filter(author=self.pk)
    

    #To filter by author.
    #queryset = Post.objects.filter(author=3) 
    # Using ForeignKey to filter.
    #queryset = Post.objects.filter(author_id=37)

    #To filter by category.
    #queryset = Post.objects.filter(category__iexact='edit category')

    #def get_queryset(self):
    #   self.author = get_object_or_404(Post, name=self.kwargs['author'])
    #   return Post.objects.filter(author=self.author)

# class AllAuthorPostsMixin():
#     """ Class to be used as a mixin to  get
#     extra database content.
#     """

#     def get_context_data(self, *args, **kwargs):
#         category_menu = PostCategory.objects.all()
#         context = super().get_context_data(*args, **kwargs)
#         context['category_menu'] = category_menu
#         return context

    
    

# class ArticleDetailView(LoginRequiredMixin, AllAuthorPostsMixin, DetailView):
#     model = Post
#     template_name = 'article_detail.html'

#     def get_context_data(self, *args, **kwargs):
#         all_author_post = Post.objects.filter(author=Post.author.id)
#         context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
#         context['all_author_post'] = all_author_post
#         return context

    # def get_context_data(self, *args, **kwargs):
    #     category_menu = PostCategory.objects.all()
    #     context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    #     context['category_menu'] = category_menu
    #     return context


    # def get_queryset(self):
    #     post_list = Post.objects.all()
    #     return post_list




# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'article_detail.html'  

#     def books(self):
#         return Post.objects.all()



def ArticleDetailView(request, pk):
    post = Post.objects.get(pk=pk)

    # Code to ouput all data in the category field.
    category_menu = PostCategory.objects.all() 
    comments = Comment.objects.filter(
        post=post.id
        ).order_by('-id')

    # Code to output all other posts of the author
    # on post detail template.
    all_author_post = Post.objects.filter(
        author=post.author.id
        ).exclude(pk=pk)

    user = get_user_model()

    # comment output ======================
    # Refactor this fucntion from here ==========
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('comment_body')
            comment = Comment.objects.create(
                post=post, 
                commentator=request.user, 
                comment_body=content
                )
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm
    # Refactor to this point.

    context = {
        'post':post, 
        'all_author_post':all_author_post, 
        'category_menu':category_menu,
        'comments':comments,
        'comment_form':comment_form
        }
    template = 'article_detail.html'
    return render(request, template, context)


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    
    #fields = '__all__' #['title', 'author', 'body']

    # Get the category list for the base.html template.
    def get_context_data(self, *args, **kwargs):
        category_menu = PostCategory.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

class UpdatePostView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        # Get the category list for the base.html template.
        category_menu = PostCategory.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user   

class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    # Forbid a user from editing and deleting posts they
    # did not create.
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Views for blog posts categories.

class AddCategoryView(LoginRequiredMixin, CreateView):
    model = PostCategory
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

    # For login redirection.
    login_url = '/account/login/'

class CategoryListView(ListView):
    model = PostCategory
    template_name = 'category_list.html'
    context_object_name = 'category_list'

class EditCategoryView(UpdateView):
    model = PostCategory
    template_name = 'edit_category.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' '))
    context =  { 
        'cats':cats.replace('-', ' '), 
        'category_posts':category_posts
        }
    # Pass the 'context' variable into the template.
    return render(request, 'categories.html', context)
    
        
# I tried to do the categories with class generic views,
# class CategoryView(ListView):
#     template_name = 'categories.html'
#     #model = Post
#     queryset = Post.objects.filter(
#         category__iexact='cats'
#     )

    # queryset = Post.objects.get(category='fuck')
    
    context_object_name = 'category_posts'

    # def get(self, request, cats, *args, **kwargs):
    #     category_posts = Post.objects.get(category='fuck')
    #     return render(category_posts)


    

   # get(pk=self.kwargs.get('pk'))