from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from registrycontrol.api import ImobiliariaViewSet, ImovelViewSet

api_router = routers.DefaultRouter()
api_router.register(r'imobiliaria', ImobiliariaViewSet)
api_router.register(r'imovel', ImovelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
]
