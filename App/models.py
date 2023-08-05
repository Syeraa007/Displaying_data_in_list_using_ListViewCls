from django.db import models

# Create your models here.
class Trainer(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    area=models.TextField()
    pin=models.IntegerField()

    def __str__(self) -> str:
        return self.name