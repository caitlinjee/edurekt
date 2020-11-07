from django.db import models

#from modules.models import Module

class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)

    #modules = models.ManyToManyField(Module, related_name='students', through='TakeModule')

    def __str__ (self):
        return "{}: {} ({}:{})".format(self.matric_number, self.name, self.year, self.course)


#class TakeModule(models.Model):
#    module = models.ForeignKey(Module, related_name='module_to_student', on_delete=models.CASCADE)
#    student = models.ForeignKey(Student, related_name='student_to_module', on_delete=models.CASCADE)
#
#    class Meta:
#        unique_together = ('module', 'student')
