from django.urls import path
from .views import (
    HomeView, 
    PostDetailView,
     AddPostView, 
     UpdatePostView,
      DeletePostView, 
      CategoryView,      
      )
from .models import Post

post_detail_path = 'slug:slug'


urlpatterns = [
    path('category/<str:cats>/', CategoryView, name='category') ,

    path('', HomeView.as_view(), name='home' ),
    path('article/<post_detail_path>', PostDetailView, name='article_detail'),
    path('article/<post_detail_path>/delete_post/', DeletePostView.as_view(), name='delete_post'),
    path('article/edit_post/<post_detail_path>/', UpdatePostView.as_view(), name='edit_post'),
    path('create_post/', AddPostView.as_view(), name='create_post'),

]
