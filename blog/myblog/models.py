from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = TaggableManager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("post", kwargs={'post_slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']

    def __str__(self):
        return self.text
