# Generated by Django 5.1.6 on 2025-03-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_tag_name_blog_tags_delete_blogtag_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
