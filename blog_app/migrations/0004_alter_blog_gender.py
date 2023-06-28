# Generated by Django 4.1.7 on 2023-04-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_blog_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=255),
        ),
    ]
