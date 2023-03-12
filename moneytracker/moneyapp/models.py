from django.db import models

# Create your models here.
class Statement(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    choices = (
            ("income", "income"),
            ("expense", "expense")
    )
    category = models.CharField(max_length=100, choices=choices, default=1)
    
    def __str__(self):
            return self.name + "| " + str(self.amount) + "| " + self.category
    
             