from django.contrib.auth import get_user_model
from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Comment, Post, PostCategory
from .forms import CommentForm, CreatePostForm, EditPostForm 

def error_404(request, exception):
    return render(request, '404.html')

class PostsCategoryMixin():
    """ Class to be used as a mixin to  get
    extra database content.
    """

    def get_context_data(self, *args, **kwargs):
        category_menu = PostCategory.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context
class HomeView(PostsCategoryMixin, ListView,):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    #paginate_by = 2


def PostDetailView(request, slug):
    post = Post.objects.get(slug__iexact=slug)

    category_menu = PostCategory.objects.all()

    comments = Comment.objects.filter(
        post=post.id
        ).order_by('-id')

    all_author_post = Post.objects.filter(
        author=post.author.id
        ).exclude(slug=slug)

    user = get_user_model()

    # comment output ======================
    # Refactor this function from here ==========
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

    context = {
        'post':post,
        'all_author_post':all_author_post,
        'category_menu':category_menu,
        'comments':comments,
        'comment_form':comment_form
        }
    template = 'article_detail.html'
    return render(request, template, context)

class AddPostView(LoginRequiredMixin,  PostsCategoryMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class UpdatePostView(UserPassesTestMixin, PostsCategoryMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePostView(UserPassesTestMixin, PostsCategoryMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    # Forbid a user from editing and deleting posts they
    # did not create.
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Views for blog posts categories.
def CategoryView(request, cats):
    category_menu = PostCategory.objects.all()
    category_posts = Post.objects.filter(
        category__name__iexact=cats.replace('-', ' ')
        )
    context =  {
        'cats':cats.replace('-', ' '),
        'category_posts':category_posts,
        'category_menu': category_menu
        }
    return render(request, 'categories.html', context)

class SearchPostsResultListView(ListView):
    context_object_name = 'post_list'
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.search(query=query)
