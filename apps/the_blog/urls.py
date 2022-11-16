from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('article/<slug:slug>', views.PostDetailView, name='article_detail'),
    path('article/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('article/edit/<slug:slug>/', views.UpdatePostView.as_view(), name='edit_post'),
    path('article/new/', views.AddPostView.as_view(), name='create_post'),
    path('search/', views.SearchPostsResultListView.as_view(), name='posts_search_results'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category')
]
