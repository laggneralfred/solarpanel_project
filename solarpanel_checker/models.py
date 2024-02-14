from django.db import models


# Create your models here.

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')  # 'images/' is a subdirectory of 'media/'
