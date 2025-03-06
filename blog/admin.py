from django.contrib import admin
from . models import CustomUser, Category, Blog, Comment
from django.contrib.auth.admin import UserAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Custom Field Heading',
            {
                'fields': (
                    'position',
                    'x_account',
                    'fb_account',
                    'github_account',
                    'linkedin_account',
                    'image',
                    'intro',
                    'about'
                ),
            },
        ),
    )


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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
