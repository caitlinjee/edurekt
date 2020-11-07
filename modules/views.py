from rest_framework import generics

# Create your views here.
from modules.models import Module
from modules.serializers import ModuleSerializer


class ModuleList(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

def addStudents(pk):
    try:
        m = Module.objects.get(pk)
        m.students.add('test')
        m.save()
    except Module.DoesNotExist:
        return "Mod doesn't exist"
        pass
    except django.db.utils.IntegrityError:
        return "test"
        pass