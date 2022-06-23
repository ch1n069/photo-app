from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100, null=True)








class Category(models.Model):
    name = models.CharField(max_length=100, null=False,)




    def __str__(self):
        return self.name

class  Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=200, null=False)


        
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.object.filter(category__icontains=search_term)


        return image

    def save_photo(self):
        self.save



    def __str__(self):
        return  self.description

