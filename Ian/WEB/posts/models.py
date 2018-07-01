from django.db import models
from datetime import datetime
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    def __str__(self):
        return self.title