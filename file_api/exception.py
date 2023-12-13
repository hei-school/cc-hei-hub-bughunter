from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_423_LOCKED


class FilenameInvalid(ValidationError):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "File name is invalid"

class FileTooLarge(ValidationError):
    status_code = HTTP_423_LOCKED
    default_detail = "File size is too large"
