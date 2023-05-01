from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import URLSerializer
from .services import UrlServices
from .models import Shortener


class UrlViewSet(viewsets.ModelViewSet):
    services = UrlServices()
    queryset = Shortener.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        long_url = request.data.get('long_url')
        self.services.save_url(long_url=long_url)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

