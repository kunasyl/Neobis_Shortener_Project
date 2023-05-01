from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from urlshortner_app.views import UrlViewSet


router = DefaultRouter()
router.register(r'', UrlViewSet, basename='urls')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]


