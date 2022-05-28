from django.contrib import admin
from photos.models import Photo, Category , Location
# Register your models here.



admin.site.register(Photo)
admin.site.register(Category)

admin.site.register(Location)

