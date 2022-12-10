from django.db import models

# Create your models here.

class Momber(models.Model):
    user_name = models.CharField(max_length=30)
    status    = models.BooleanField(default=False)
    message   = models.TextField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self .user_name

class MSG(models.Model):
    message = models.TextField(null=True)

    def __str__(self):
        return self.message