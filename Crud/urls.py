from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.UserAddShowView.as_view(), name='index'),
    # path("", views.add_show, name="index"),
    path("delete/<int:id>", views.UserDeleteView.as_view(), name="deletedata"),
    path("<int:id>", views.UserUpdateView.as_view(), name="updatedata")
]