from rest_framework import serializers
from registrycontrol.models import Imobiliaria, Imovel


class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliaria
        fields = "__all__"

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = "__all__"

