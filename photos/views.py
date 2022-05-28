from django.shortcuts import render
from photos.models import Photo, Category , Location

# Create your views here.





def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    ctx = {'categories':categories, 'photos':photos}
    return render(request, 'photos/gallery.html',ctx)



def ViewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    ctx = {'photo':photo,}

    return render(request, 'photos/photo.html', ctx)
