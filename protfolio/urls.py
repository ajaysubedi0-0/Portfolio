from django.urls import path
from .views.main_view import home,about,contact
urlpatterns = [
    path("",home),
    path("about",about),
    path("contact",contact),
]
