from django.db import models

# Create your models here.
class Dish(models.Model):
    id : int
    name : str
    img : str
    desc : str
    price : int