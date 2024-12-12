from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)


from ..serializer.user_serializer import UserSerializer
from django.contrib.auth.models import User
class UserViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['usuario']

    # def update(self, request, *args, **kwargs):
    #     self.serializer_class = ProductoUpdateSerializer
    #     response = super().update(request, *args, **kwargs)
    #
    #     # # Registra el cambio
    #     # objeto = self.get_object()
    #     # mensaje = "Producto actualizado"
    #     # registrarCambio(request, objeto, mensaje)
    #     #
    #     # return response


