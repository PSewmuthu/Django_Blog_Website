from django.contrib import admin
from . models import Category, Blog, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'image',
                    'status', 'featured_status', 'tag_list', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'slug', 'category',
                     'status', 'featured_status')
    list_editable = ('status', 'featured_status')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'full_name', 'email', 'website',
                    'comment', 'created_at', 'updated_at')
    search_fields = ('blog__title', 'blog__slug', 'full_name',
                     'email', 'website', 'comment')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
