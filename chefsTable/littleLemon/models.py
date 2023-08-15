from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_id = models.CharField(max_length=3)
    menu_item = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
