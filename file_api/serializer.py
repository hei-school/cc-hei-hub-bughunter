from rest_framework import serializer

from file_api.models import File

class FileSerializer(serializer.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'