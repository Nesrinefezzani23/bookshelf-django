from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    publication_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='books', blank=True)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.book} ({self.rating})"

User = get_user_model()
User.add_to_class('favorites', models.ManyToManyField(Book, related_name='favorited_by', blank=True))