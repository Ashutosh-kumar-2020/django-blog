from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=64)
    issue_type = models.CharField(max_length=200)
    desc  = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return "Message from " + self.name + ' - ' + self.email

    