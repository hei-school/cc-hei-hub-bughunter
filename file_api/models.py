from django.core.validators import FileExtensionValidator
from django.db import models

from file_api.validators import validate_file_name


class File(models.Model):
    file = models.FileField(upload_to='file_api', validators=[
        validate_file_name,
        FileExtensionValidator(["pdf", "doc", "jpg", "png", "jpeg", "gif", "tiff", "mp4", "mov", "mpeg", "movw"])
    ])


class Image(models.Model):
    image = models.ImageField(upload_to='file_api/img')
