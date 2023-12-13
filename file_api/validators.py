from .exception import FilenameInvalid


def validate_file_name(file_name: str):
    if len(file_name) > 100:
        raise FilenameInvalid("File name too long, file name length must be less than 100 characters.")
