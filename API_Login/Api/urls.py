from django.urls import path
from Api import views

urlpatterns = [
    path("", views.index, name="index"),
]