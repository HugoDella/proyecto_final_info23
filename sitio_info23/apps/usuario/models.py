from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.



"""Se realizaran los models"""
class Usuario(AbstractUser):
    imagen= models.ImageField(null= True, blank=True, upload_to="usuario",default="usuario/user-default.png")

    def get_absolute_url(self):
        return reverse("index")

# class Post(models.Model):
#     titulo= models.CharField(max_length=50, null=False)
#     subtitulo=models.CharField(max_length=100, null=True, blank= True)
#     fecha=models.DateTimeField(null=False)
#     texto=models.TextField(null=False)
#     activo=models.BooleanField(default=True)
#     categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default= "sin categoria")
#     imagen=models.ImageField(null=True, blank=True, upload_to= "media", default="static/post_default.png")
#     publicado= models.DateTimeField(default= timezone.now)

#     class Meta:
#         ordering= ('-publicado',)

#     def __str__(self):
#         return self.titulo

#     def delete(self, using= None, keep_parents= False):
#         self.imagen.delete(self.imagen.name)
#         super().delete() 


