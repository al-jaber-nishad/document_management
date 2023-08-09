
from rest_framework import serializers
from .models import Document

class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def validate_file(self, value):
        allowed_formats = ['pdf', 'docx', 'txt']  # Add more formats as needed
        format = value.name.split('.')[-1].lower()
        
        if format not in allowed_formats:
            raise serializers.ValidationError("Invalid file format. Supported formats: " + ", ".join(allowed_formats))
        
        return value

