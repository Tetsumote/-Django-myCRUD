from django.db import models

from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_edit',kwargs={'pk':self.pk})
