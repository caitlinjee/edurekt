from rest_framework import serializers

from ccas.models import CCA
from students.models import Student, JoinCCA


class StudentSerializer(serializers.ModelSerializer):
    ccas = serializers.PrimaryKeyRelatedField(many=True, queryset=CCA.objects.all(), read_only=False)

    class Meta:
        model = Student
        fields = ('matric_number', 'name', 'year', 'course', 'membership_status', 'ccas')


class JoinCCASerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinCCA
        fields = ('cca', 'student')