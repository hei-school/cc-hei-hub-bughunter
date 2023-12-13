from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet

from file_api.serializer import FileSerializer
from .models import File


class FileUploadView(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer
    queryset = File.objects.all()
