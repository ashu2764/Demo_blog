# Generated by Django 4.1.7 on 2023-03-29 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='sub',
            new_name='submit',
        ),
    ]
