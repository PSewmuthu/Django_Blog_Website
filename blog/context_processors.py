from . models import Category, CustomUser
from django.db.models import Count


def get_categories_counts(request):
    categories = Category.objects.annotate(
        posts_count=Count('blog')).order_by('-posts_count')
    return dict(categories=categories)


def get_author(request):
    author = CustomUser.objects.all().first()

    return dict(author=author)
