from . models import PostCategory

#query the PostCategory model for its values.
CATEGORY_CHOICES = PostCategory.objects.all().values_list('name', 'name')


def category_choices():

    choices_list = []

    for choice in CATEGORY_CHOICES:
        choices_list.append(choice)

    return choices_list