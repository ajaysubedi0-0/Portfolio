from django.urls import path
from .views.main_view import home,create,edit,delete,single_blog
from .views.auth_view import login

urlpatterns = [
    path("",home),
    path("create",create),
    path("edit",edit),
    path("delete",delete),
    path("login",login), 
    path("single",single_blog),
]
