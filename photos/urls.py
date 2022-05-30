from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.ViewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('search/', views.search_results, name='search_results'),
    path('update/<str:pk>/', views.updatePhoto, name='update-photo'),



]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)