from django.db import models

# Create your models here.
from django.db import models

class Players(models.Model):
    name_of_person = models.CharField(max_length=254, null=True, blank=True)
    current_score = models.IntegerField(null=True, blank=True)
   
    def __str__(self):
        return self.name_of_person

