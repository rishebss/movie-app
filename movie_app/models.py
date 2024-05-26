from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    username=models.CharField(max_length=250)
    year=models.TextField()
    trailer=models.URLField(blank=True,null=True)
    img=models.ImageField(upload_to='gallery')
    moviereview=models.CharField(max_length=250)

    def __str__(self):
        return self.name

# class Review(models.Model):
#     moviename = models.CharField(max_length=250)
#     moviereview = models.CharField(max_length=250)
#     author = models.CharField(max_length=250)

    # def __str__(self):
    #     return self.moviename