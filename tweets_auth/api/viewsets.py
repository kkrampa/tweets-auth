from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny

from tweets_auth.api.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = UserSerializer

    queryset = User.objects.all()

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        return self.create(request)
