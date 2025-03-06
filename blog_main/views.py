from django.shortcuts import render, redirect
from django.db.models import Count
from blog.models import Blog, Category, CustomUser
from taggit.models import Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    large_featured_posts = Blog.objects.filter(
        featured_status='large', status='published').order_by('-created_at')[:5]
    small_featured_posts = Blog.objects.filter(
        featured_status='small', status='published').annotate(number_of_comments=Count('comment'))
    posts = Blog.objects.filter(
        featured_status='none', status='published').order_by('-created_at')[:6]

    context = {
        'large_featured_posts': large_featured_posts,
        'small_featured_posts': small_featured_posts,
        'posts': posts
    }

    return render(request, 'home.html', context)


def category(request, category_id):
    posts = Blog.objects.filter(status='published', category=category_id)
    paginator = Paginator(posts, 15)

    page_number = request.GET.get('page')
    try:
        # returns the desired page object
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    context = {
        'posts': page_obj,
        'category': category
    }

    return render(request, 'category.html', context)


def tag(request, tag_id):
    posts = Blog.objects.filter(status='published', tags=tag_id)
    paginator = Paginator(posts, 15)

    page_number = request.GET.get('page')
    try:
        # returns the desired page object
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    try:
        tag = Tag.objects.get(pk=tag_id)
    except:
        return redirect('home')

    context = {
        'posts': page_obj,
        'tag': tag
    }

    return render(request, 'tag.html', context)


def categories(request):
    categories = Category.objects.all()
    posts = []
    for category in categories:
        post = Blog.objects.filter(
            status='published', category=category.pk).last()
        posts.append(post)

    recent_posts = Blog.objects.filter(
        status='published').order_by('-created_at')[:5]

    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'tags': tags
    }

    return render(request, 'categories.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(body__icontains=keyword), status='published')
    paginator = Paginator(posts, 15)

    page_number = request.GET.get('page')
    try:
        # returns the desired page object
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'posts': page_obj,
        'size': len(posts),
        'keyword': keyword
    }

    return render(request, 'search.html', context)


def author_profile(request):
    user = CustomUser.objects.all().first()
    posts_count = Blog.objects.filter(status='published').count()
    categories_count = Category.objects.all().count()
    tags_count = Tag.objects.all().count()
    features_posts = Blog.objects.filter(
        featured_status='large', status='published').annotate(number_of_comments=Count('comment')).order_by('-created_at')[:2]

    context = {
        'user': user,
        'posts_count': posts_count,
        'categories_count': categories_count,
        'tags_count': tags_count,
        'features_posts': features_posts
    }

    return render(request, 'author-profile.html', context)


def contacts(request):
    return render(request, 'contact.html')
