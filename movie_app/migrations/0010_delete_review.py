# Generated by Django 5.0.3 on 2024-03-07 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_review_remove_movie_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]