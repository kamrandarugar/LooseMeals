from django.contrib import admin

# Register your models here.
from .models import UploadFile, File, Image, Review

admin.site.register(UploadFile)

admin.site.register(File)

admin.site.register(Image)

admin.site.register(Review)

