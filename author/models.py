from django.db import models

# Create your models here.
class Author(models.Model):
   
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name_address

    @property
    def name_address(self) -> str:
        return f"{self.name} | {self.age}"
