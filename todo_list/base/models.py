from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=200, null=True, blank=True) # Title/name of task
    description = models.TextField(null=True, blank=True) # about the task
    complete = models.BooleanField(default=False) # for completion status, starting value would be 'not completed'
    created = models.DateTimeField(auto_now_add=True) # for task creation timestamp

    # func to display title as object name in admin panel
    def __str__(self):
        return self.title

    # User-specific data storage
    class Meta:
        order_with_respect_to = 'user'
