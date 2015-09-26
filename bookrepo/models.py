from django.db import models

class Book(models.Model):
    author=models.ForeignKey('auth.User')
    bookname=models.CharField(max_length=200)
    review=models.TextField()
    #update_date=models.DateTimeField()

    def __str__(self):
        return self.bookname


# Create your models here.
