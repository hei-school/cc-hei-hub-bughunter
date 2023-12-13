from .exception import FilenameInvalid, FileTypeNotSupported, SensitiveFileNotAllowed, IllegalFileContentNotAllowed
import magic
import re


def validate_file_name(file_name: str):
    if len(file_name) > 100:
        raise FilenameInvalid("File name too long, file name length must be less than 100 characters.")


def check_file_type(file):
    ALLOWED_MIME_TYPES = {
        'application/pdf',
        'image/*',
        'image/*',
        'video/*',
    }
    mime_type = magic.Magic()
    detected_type = mime_type.from_file(file)
    if detected_type not in ALLOWED_MIME_TYPES:
        raise FileTypeNotSupported()


def check_sensitive_information(file):
    file_content = file.read()

    sensitive_patterns = ['username', 'password', 'AWS_ACCESS_KEY_ID', 'AW_SECRET_ACCESS_KEY']

    for pattern in sensitive_patterns:
        if re.search(pattern, file_content):
            raise SensitiveFileNotAllowed()


def check_illegal_information(file):
    file_content = file.read()

    illegal_pattern = ['porn', 'xxx', 'adult', 'NSFW', 'sex',
                       'racism', 'hate', 'threat', 'discrimination',
                       'violence', 'kill', 'murder', 'assault',
                       'drug', 'weapon', 'hacking', 'theft', 'murder',
                       'discriminatory', 'sexist', 'homophobic', 'racist',
                       'extremism', 'terrorism', 'radicalization',
                       'defamation', 'slander', 'lie',
                       'dangerous', 'risky', 'harmful']

    for pattern in illegal_pattern:
        if re.search(pattern, file_content):
            raise IllegalFileContentNotAllowed()
