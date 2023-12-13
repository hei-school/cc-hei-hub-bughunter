from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from file_api.serializer import FileSerializer
from .models import File


class FileUploadView(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer
    queryset = File.objects.all()


class FileUploadItemView(APIView):
    def get(self, request, pk):
        try:
            file = File.objects.get(pk=pk)
            serializer = FileSerializer(file)
        except File.DoesNotExist:
            return Response({f"message": f"File with id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
