from django.db import models

# Create your models here.
class API_Login(models.Model):
    STATUS_CHOICES = [
        ("N", "Não iniciado"),
        ("P", "Pendente"),
        ("C", "Concluído"),
    ]
    
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255) 
    age  = models.IntegerField(default= 0)
    
    def __str__(self) -> str:
        return self.title
    
class API_Login_Pessoas(models.Model):
    pessoa = models.CharField(max_length=255)
    nome   = models.CharField(max_length=255)
    genero = models.CharField(max_length=16)