# Generated by Django 4.2.8 on 2024-01-05 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blog_delete_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='subTitle',
        ),
    ]
