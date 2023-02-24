from rest_framework import serializers
from .models import Work, Artist

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link','work_type']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name','work']
