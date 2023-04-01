from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_address = models.TextField()
    emp_phone = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    def __str__(self):
        return self.emp_name