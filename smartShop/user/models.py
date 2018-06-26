from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    clothes = models.ManyToManyField('clothing.Clothing')

    def __str__(self):
        return 'User: ' + self.username