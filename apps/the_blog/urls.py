from django.urls import path
from .views import (
    HomeView, 
    ArticleDetailView,
     AddPostView, 
     UpdatePostView,
      DeletePostView, 
      AddCategoryView, 
      CategoryListView,
      EditCategoryView,
      CategoryView,
      #ArticleListView,
      
      )
from .models import Post

urlpatterns = [
    #path('', views.home, name='home'),
    path('category/<str:cats>/', CategoryView, name='category') ,


    path('edit_category/<int:pk>/', EditCategoryView.as_view(), name='edit_category'),

    path('category_list/', CategoryListView.as_view(), name='category_list'),

    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    path('article/<int:pk>/delete_post/', DeletePostView.as_view(), name='delete_post'),

    path('article/edit_post/<int:pk>/', UpdatePostView.as_view(), name='edit_post'),

    path('new_blog_post/', AddPostView.as_view(), name='create_post'),

    # path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),


    # Path for function detail view.
    path('article/<int:pk>', ArticleDetailView, name='article_detail'),
    # path('article/<int:pk>', add_comment, name='add_comment'),
    
    #path for function list view on detail view.
    #  path('article/', ArticleListView, name='article_list2'),

    path('', HomeView.as_view(), name='home' )


]