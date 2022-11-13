from django.db import models
from django.urls import reverse
# Create your models here.
class Data(models.Model):
    phone = models.PositiveIntegerField(max_length=12)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"Parol: {self.password} phone: {self.phone}"

    def get_absolute_url(self):
        return reverse('add')
