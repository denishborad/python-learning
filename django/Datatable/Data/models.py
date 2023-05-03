from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname
    
    def get_data(self):
        return{
            "sr_no"     :   self.id,
            "firstname" :   self.firstname,
            "lastname"  :   self.lastname,
            "address"   :   self.address,
        }