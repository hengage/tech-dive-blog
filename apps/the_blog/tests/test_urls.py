from django.test import SimpleTestCase
from django.urls import resolve, reverse
from the_blog.views import (CategoryView,  DeletePostView)

class TestCategoryUrls(SimpleTestCase):

    def test_category_url_is_resolved(self):
        url = reverse('category', args=['cats'])
        self.assertEquals(resolve(url).func, CategoryView)


class TestArticleUrls(SimpleTestCase):

    def test_delete_post_url_is_resolved(self):
        url = reverse('delete_post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, DeletePostView)
