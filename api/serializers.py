from rest_framework import serializers

from .models import Persona,Cliente

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('name', 'genero','identificacion','tipo_identificacion')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','name', 'genero','identificacion','tipo_identificacion','fecha_residencia','estado_civil','num_cargas_faml','tipo_cliente')