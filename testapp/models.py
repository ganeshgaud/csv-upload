from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=64)
    college_name=models.CharField(max_length=64)
    std_cell_no=models.BigIntegerField()
    emai_id=models.EmailField()

    def __str__(self):
        return self.username
