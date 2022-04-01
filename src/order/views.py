from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from order.models import OrderTime
from order.serializers import OrderTimeSerializer


class OrderTimeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = OrderTimeSerializer
    queryset = OrderTime.objects.all()

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (AllowAny,)
        return super().get_permissions()
