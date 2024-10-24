from django.db import models

# Create your models here.
class Greeting(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.message
