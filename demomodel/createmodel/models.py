from django.db import models

# Create your models here.
class details(models.Model):
    empid=models.IntegerField(max_length=70)
    empfname=models.CharField(max_length=70)
    emplname=models.CharField(max_length=70)
    empemail=models.EmailField()
    empaddress=models.CharField(max_length=70)
