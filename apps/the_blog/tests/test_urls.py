from django.test import SimpleTestCase
from django.urls import resolve, reverse
from the_blog.views import (CategoryView, CategoryListView,
EditCategoryView, AddCategoryView,
DeletePostView)

class TestTheBlogCategoryUrls(SimpleTestCase):

    def test_category_url_is_resolved(self):
        url = reverse('category', args=['cats'])
        self.assertEquals(resolve(url).func, CategoryView)

    def test_edit_category_url_is_resolved(self):
        url = reverse('edit_category', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditCategoryView)

    def test_category_list_url_is_resolved(self):
        url = reverse('category_list')
        self.assertEquals(resolve(url).func.view_class, CategoryListView)

    def test_add_category_url_is_resolved(self):
        url = reverse('add_category')
        self.assertEquals(resolve(url).func.view_class, AddCategoryView)

class TestTheBlogArticleUrls(SimpleTestCase):

    def test_delete_post_url_is_resolved(self):
        url = reverse('delete_post', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeletePostView)
