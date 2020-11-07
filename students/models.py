from django.db import models

from modules.models import Module
from ccas.models import CCA

from django.core.validators import RegexValidator

status = RegexValidator(r'^[M|L]*$', 'Only member or leader are allowed.')


class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)
    membership_status = models.CharField(max_length=1, blank=False, validators = [status])

    modules = models.ManyToManyField(Module, related_name='students', through='TakeModule')
    ccas = models.ManyToManyField(CCA, related_name='students', through='JoinCCA')

    def __str__ (self):
        return "{}: {} ({}:{}) {}".format(self.matric_number, self.name, self.year, self.course, self.membership_status)


class TakeModule(models.Model):
    module = models.ForeignKey(Module, related_name='module_to_student', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_to_module', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('module', 'student')

class JoinCCA(models.Model):
    cca = models.ForeignKey(CCA, related_name='cca_to_student', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_to_cca', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cca', 'student')

