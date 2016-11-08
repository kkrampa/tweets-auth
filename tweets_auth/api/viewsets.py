from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from tweets.models import Tweet
from tweets_auth.api.serializers import UserSerializer, TweetSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = UserSerializer

    queryset = User.objects.all()

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        return self.create(request)

    @list_route(methods=['get'], permission_classes=[AllowAny])
    def check_username_availability(self, request):
        available = False

        if 'username' not in request.GET:
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            User.objects.get(username=request.GET['username'])
        except User.DoesNotExist:
            available = True
        return Response(
            {'available': available}
        )


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
