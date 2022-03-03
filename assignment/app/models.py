from django.db import models


# Create your models here.

class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    check_in = models.CharField(max_length=200, null=False)
    check_out = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
