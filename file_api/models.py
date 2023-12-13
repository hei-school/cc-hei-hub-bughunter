from django.db import models

from file_api.validators import validate_file_name


class File(models.Model):
    file = models.FileField(upload_to='file_api', validators=[validate_file_name])


class Image(models.Model):
    image = models.ImageField(upload_to='file_api/img')
