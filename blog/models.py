from django.db import models
from django.template.defaultfilters import slugify
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

FEATURED_CHOICE = (
    ('none', 'None'),
    ('small', 'Small'),
    ('large', 'Large')
)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def _get_slug(self):
        return slugify(self.title)

    slug = property(_get_slug)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=1000)
    body = CKEditor5Field(config_name='extends')
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICE, default='draft')
    featured_status = models.CharField(
        max_length=100, choices=FEATURED_CHOICE, default='draft')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=100, null=False)
    email = models.EmailField(null=False)
    website = models.URLField(null=True)
    comment = models.TextField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
