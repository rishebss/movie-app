# Generated by Django 5.0.3 on 2024-03-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0004_rename_image_bio_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='biography',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
