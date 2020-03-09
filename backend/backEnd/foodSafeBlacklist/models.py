from django.db import models

# Create your models here.
class foodSafe_blacklist(models.Model):
    enterprise_name = models.CharField(max_length=30)
    legal_rep = models.CharField(null=True,blank=True,max_length=30)
    punishment = models.TextField(null=True,blank=True)
    criminal_behavior = models.TextField(null=True,blank=True)
	

