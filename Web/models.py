from django.db import models

# Create your models here.
class UploadFile(models.Model):
    info = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    image = models.FileField(upload_to='files/')

class File(models.Model):
    name = models.CharField(max_length=10000)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uri        = models.ImageField(upload_to='images/')
