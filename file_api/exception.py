from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS


class FilenameInvalid(ValidationError):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "File name is invalid"


class FileTypeNotSupported(ValidationError):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "File not supported"


class SensitiveFileNotAllowed(ValidationError):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "File with sensitive information are not allowed"


class IllegalFileContentNotAllowed(ValidationError):
    status_code = HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
    default_detail = "File not allowed due to illegal content"
