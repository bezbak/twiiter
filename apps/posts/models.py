from django.db import models
from apps.users.models import User
# Create your models here.
class Posts(models.Model):
    text = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='post_video/',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='post_image/',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        related_name='user_post',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

class Like(models.Model):
    post = models.ForeignKey(
        Posts,
        related_name='like_post',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='like_user',
        on_delete=models.CASCADE
    )

class Comment(models.Model):
    post = models.ForeignKey(
        Posts,
        related_name='comment_post',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='comment_user',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=255
    )
    created = models.DateTimeField(
        auto_now_add=True
    )