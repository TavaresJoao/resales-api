from rest_framework import viewsets
from registrycontrol.models import Imobiliaria, Imovel
from registrycontrol.serializers import ImobiliariaSerializer, ImovelSerializer


class ImobiliariaViewSet(viewsets.ModelViewSet):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
