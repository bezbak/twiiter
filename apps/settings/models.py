from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=20   
    )
    logo = models.ImageField(
        upload_to='logo/'
    )
    phone_number = models.CharField(
        max_length=25
    )
    email = models.EmailField(
        max_length=50
    )
    facebook = models.URLField()
    twitter = models.URLField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'