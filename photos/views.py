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



def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST 
        image  = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = category.objects.get_or_create(name=data['category_new'])
        else:
            category = None



        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )
    ctx = {'categories':categories}

    return render (request , 'photos/add.html', ctx)