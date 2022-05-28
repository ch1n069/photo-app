from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False)



    def __str__(self):
        return self.name





class Category(models.Model):
    name = models.CharField(max_length=100, null=False,)




    def __str__(self):
        return self.name

class  Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=False)
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=200, null=False)

