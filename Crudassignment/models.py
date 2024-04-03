from django.db import models

# Create your models here.
class Emp(models.Model):
    ename = models.CharField(max_length=50)
    elocation = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.ename
    
    class meta:
        db_table = "Emp"
        