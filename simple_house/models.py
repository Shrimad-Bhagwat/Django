from django.db import models

# Create your models here.
class Dish(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    discount = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Dish'