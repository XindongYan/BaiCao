from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

Person.objects.create(name = "xindong yan", age = "19")

# Create your models here.
