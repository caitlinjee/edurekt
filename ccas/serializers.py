from rest_framework import serializers

from ccas.models import CCA

class CCASerializer(serializers.ModelSerializer):
    class Meta:
        model = CCA
        fields = ('code', 'name', 'description')