from django.shortcuts import render
from django.db.models import Count
from blog.models import Blog, Category


def home(request):
    large_featured_posts = Blog.objects.filter(
        featured_status='large', status='published')
    small_featured_posts = Blog.objects.filter(
        featured_status='small', status='published').annotate(number_of_comments=Count('comment'))
    posts = Blog.objects.filter(
        featured_status='none', status='published').order_by('created_at')

    context = {
        'large_featured_posts': large_featured_posts,
        'small_featured_posts': small_featured_posts,
        'posts': posts
    }

    return render(request, 'home.html', context)
