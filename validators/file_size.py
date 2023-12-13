from django.core.exceptions import ValidationError
from django.core.validators import FileValidator
from django.utils.translation import ugettext_lazy as _

def validate_file_size(file):
    max_size = 52428800 # 50 MB

    validator = FileValidator(max_size=max_size)

    if file.size > max_size:
        raise FileTooLarge

    validator(file)