# Generated by Django 5.1.6 on 2025-03-04 19:11

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
