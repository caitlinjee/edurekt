from django.db import models

class CCA(models.Model):
    code = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)

    def __str__ (self):
        return "{}: {} {}".format(self.code, self.name, self.description)
