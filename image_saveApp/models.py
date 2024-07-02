from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    pass

    def __str__(self):
        return f'Email: {self.email}, Senha: {self.password}'

class Image(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_images/')
    legend = models.CharField(max_length=200, blank=True)
    image_path = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.image.name[:50] + "..."