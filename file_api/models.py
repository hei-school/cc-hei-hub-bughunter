from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='file_api')


class Image(models.Model):
    image = models.ImageField(upload_to='file_api/img')
