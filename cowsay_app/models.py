from django.db import models

# Create your models here.


class Message(models.Model):
    message = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.message}"
