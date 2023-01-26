from django.db import models

# Create your models here.


class Game(models.Model):

    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField('Date')
    platform = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=250)
    favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
