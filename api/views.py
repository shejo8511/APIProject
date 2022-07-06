from rest_framework import viewsets

from .serializers import PersonaSerializer,ClienteSerializer
from .models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('tipo_identificacion')
    serializer_class = ClienteSerializer