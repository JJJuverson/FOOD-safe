from django.db import models

# Create your models here.
class foodSafe_cases(models.Model):
    case_name = models.CharField(max_length=30)
    offender = models.CharField(max_length=30)
    gender = models.BooleanField(default=True)
    age = models.IntegerField(default=0)
    domicile = models.CharField(null=True,blank=True,max_length=30)
    criminal_behavior = models.CharField(max_length=50)
	



    def __str__(self):
        return self.case_name

	
	
	