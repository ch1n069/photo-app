from django.shortcuts import render
from photos.models import Photo, Category , Location

# Create your views here.





def gallery(request):
    categories = Category.objects.all()
    ctx = {'categories':categories}
    return render(request, 'photos/gallery.html',ctx)



def ViewPhoto(request, pk):
    return render(request, 'photos/photo.html')
