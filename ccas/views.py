from rest_framework import generics

# Create your views here.
from ccas.models import CCA
from ccas.serializers import CCASerializer


class CCAList(generics.ListCreateAPIView):
    queryset = CCA.objects.all()
    serializer_class = CCASerializer


class CCADetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CCA.objects.all()
    serializer_class = CCASerializer