from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from . models import Blog, Comment
from taggit.models import Tag


def blog(request, slug):
    post = get_object_or_404(Blog, slug=slug, status='published')

    if request.method == "POST":
        comment = Comment()
        comment.blog = post
        comment.full_name = request.POST['full_name']
        comment.email = request.POST['email']
        comment.website = request.POST['website']
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=post)
    comment_count = comments.count()
    recent_posts = Blog.objects.filter(
        status='published').order_by('-created_at')[:5]
    tags = Tag.objects.all()

    context = {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'recent_posts': recent_posts,
        'tags': tags
    }

    return render(request, 'blog.html', context)
