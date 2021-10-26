from django.db import models

# Create your models here.
class Printer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    buildheight = models.IntegerField()

   
    def __str___(self):
        return self.name