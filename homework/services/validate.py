from django.core.exceptions import ValidationError

class FileValidate:
    @staticmethod
    def file_size(value):
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MiB.')