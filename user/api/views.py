from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer
from ..models import Customer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

