from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from the_blog.views import (
    CategoryView,
    DeletePostView, 
    AddPostView,
    PostDetailView,
    UpdatePostView
)

class TestCategoryUrls(SimpleTestCase):

    def test_category_url_is_resolved(self):
        url = reverse('category', args=['cats'])
        self.assertEquals(resolve(url).func, CategoryView)


class TestArticleUrls(SimpleTestCase):

    def test_create_post_url_is_resolved(self):
        url = reverse('create_post')
        self.assertEquals(resolve(url).func.view_class, AddPostView)

    def test_post_detail_url_is_resolved(self):
        url = reverse('article_detail', kwargs={'slug':'slug'})
        self.assertEquals(resolve(url).func, PostDetailView)

    def test_edit_post_url_is_resolved(self):
        url = reverse('edit_post', kwargs={'slug':'slug'})
        self.assertEquals(resolve(url).func.view_class, UpdatePostView)

    def test_delete_post_url_is_resolved(self):
        url = reverse('delete_post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, DeletePostView)