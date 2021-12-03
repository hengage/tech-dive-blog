from django.db.models.enums import Choices
from django.test import TestCase
from the_blog.forms import CreatePostForm, EditPostForm

class TestCreatePostForm(TestCase):

    def setUp(self):
        self.form = CreatePostForm(data={
            'title': 'post title',
            'description': 'post description', 
            'category': 'django',
            'body': 'The body of the post',
        })


    def test_form_data_is_valid(self):
        
        print(self.form.data)
        print(self.form.errors)
        self.assertTrue(self.form.is_valid())

    def test_fields_are_equal(self):
        self.assertEqual(self.form.data['title'], 'post title')
        self.assertEqual(self.form.data['description'], 'post description')
        self.assertEqual(self.form.data['category'], 'django')
        self.assertEqual(self.form.data['body'], 'The body of the post')
    

    def test_form_data_is_not_valid(self):
        form = CreatePostForm(data={})

        print(form.data)
        print(form.errors)

        self.assertEquals(len(form.errors), 4)
        self.assertFalse(form.is_valid())


class TestEditPostForm(TestCase):

    def setUp(self):
        self.form = EditPostForm(data={
            'title': 'post title',
            'description': 'post description', 
            'category': 'django',
            'body': 'The body of the post',
        })

    def test_form_data_is_valid(self):
        print(self.form.data)
        print(self.form.errors)
        self.assertTrue(self.form.is_valid())