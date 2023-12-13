from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST


class FilenameInvalid(ValidationError):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "File name is invalid"
