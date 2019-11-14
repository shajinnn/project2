from django.db import models

# Create your models here.

class Product(models.Model):
    prodctname = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.prodctname