# Views
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer


class UserView(ModelViewSet):
    """UserView set

    Automatic serving post/get/put/patch/delete requests

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
