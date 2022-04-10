from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from technician.models import Technician
from technician.serializers import TechnicianSerializer


class TechnicianView(CreateAPIView):
    serializer_class = TechnicianSerializer
    queryset = Technician.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {"detail": "Your request is submitted!"},
            status=status.HTTP_201_CREATED,
        )
