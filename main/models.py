from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(verbose_name="Task Text")
    is_completed = models.BooleanField(default=False, verbose_name="Is Completed")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")


    def __str__(self):
        return f"{self.text[:50]}{'...' if len(self.text) > 50 else ''}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
