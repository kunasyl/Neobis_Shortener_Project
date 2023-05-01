from rest_framework import serializers

from . import models


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)

    class Meta:
        model = models.Shortener
        fields = ('long_url', 'short_url')

