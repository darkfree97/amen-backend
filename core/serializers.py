from rest_framework import serializers
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Publication
        fields = "__all__"
