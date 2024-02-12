from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    created_at=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    username=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Role(models.Model):
    TYPE_CHOISE=[
        ('admin','Admin'),
        ('staff','Staff'),
        ('user','User')
    ]
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=20,choices=TYPE_CHOISE)