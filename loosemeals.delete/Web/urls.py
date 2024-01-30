from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "Web"
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("contact", views.contact, name="contact"),
    path("ratings", views.ratings, name="ratings"),
    path("about", views.about, name="about"),
    

]
