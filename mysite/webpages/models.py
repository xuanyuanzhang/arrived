from django.db import models

# Create your models here.
class viewer(models.Model):
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address