from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length= 100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(
        max_length=6,
        choices= [('Male','Male'), ('Female', 'Female'), ('Other', 'Other')],
        default= 'Female'
    )
    pronouns = models.CharField(max_length=100)
    birthdate = models.DateField()
    department = models.CharField(
        max_length=50,
        choices= [('Accounting & Finance', 'Accounting & Finance'),('Advertising & Marketing', 'Advertising & Marketing'),('Graphic Design', 'Graphic Design'), 
                  ('Human Resources','Human Resources'),('IT', 'IT')],
        default = 'Accounting & Finance'
    )
    salary = models.IntegerField()
    cover = models.ImageField(upload_to= "images", blank= True)
    
    
    def __str__(self):
        return self.fname + " " + self.lname
    
    