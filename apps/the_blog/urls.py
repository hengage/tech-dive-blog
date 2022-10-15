from django.urls import path
from .views import (
    HomeView, 
    PostDetailView,
    AddPostView, 
    UpdatePostView,
    DeletePostView, 
    SearchPostsResultListView      
)


urlpatterns = [

    path('', HomeView.as_view(), name='home' ),
    path('article/<slug:slug>', PostDetailView, name='article_detail'),
    path('article/<slug:slug>/delete_post/', DeletePostView.as_view(), name='delete_post'),
    path('article/edit_post/<slug:slug>/', UpdatePostView.as_view(), name='edit_post'),
    path('create_post/', AddPostView.as_view(), name='create_post'),
    path('search/', SearchPostsResultListView.as_view(), name='posts_search_results'),
]
