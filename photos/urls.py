from django.urls import path 
from photos import views



urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("photo/<str:pk>/", views.ViewPhoto, name="photo")


]