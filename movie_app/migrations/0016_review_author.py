# Generated by Django 5.0.3 on 2024-03-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.CharField(default='admin', max_length=250),
            preserve_default=False,
        ),
    ]