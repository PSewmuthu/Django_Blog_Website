# Generated by Django 5.1.6 on 2025-03-04 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
