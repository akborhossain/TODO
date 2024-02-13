from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=5000)
    created_at=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    updated_at=models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_tasks')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned')
    def __str__(self):
        return self.title
    
class Role(models.Model):
    TYPE_CHOICES=[
        ('admin','Admin'),
        ('staff','Staff'),
        ('user','user')
    ]
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=10, choices=TYPE_CHOICES)