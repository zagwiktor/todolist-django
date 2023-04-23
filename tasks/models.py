from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_to_do = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
