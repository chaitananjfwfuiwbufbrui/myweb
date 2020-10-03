from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=20,null=True)
    subject1 = models.TextField(null=True)
    message1 =models.TextField(null=True)
    def __str__(self):
                return self.subject1
