from django.shortcuts import render ,redirect
from photos.models import Photo, Category , Location

# Create your views here.





def gallery(request):
    category = request.GET.get('category')
    if  category == None:

        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__icontains=category)
    



    categories = Category.objects.all()
   
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
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None



        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )
        return redirect('gallery')


    ctx = {'categories':categories}

    return render (request , 'photos/add.html', ctx)