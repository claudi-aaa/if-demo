from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.DateField()
    summary = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='uploads')
    tags = models.ManyToManyField(Tag)
    content = QuillField()

    def get_absolute_url(self):
        return f'/posts/{self.slug}'

    def __str__(self):
        return f'{self.title} - {self.date}'


class Freebie(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.DateField()
    summary = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='uploads')
    tags = models.ManyToManyField(Tag)
    canva_link = models.URLField(max_length=400, blank=True)
    google_link = models.URLField(max_length=400, blank=True)
    dropbox_link = models.URLField(max_length=400, blank=True)
    content = QuillField()

    def get_absolute_url(self):
        return f'/freebies/{self.slug}'


    def __str__(self):
        return f'{self.title} - {self.date}'



