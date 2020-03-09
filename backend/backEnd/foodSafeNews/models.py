from django.db import models

# Create your models here.
class foodSafe_news(models.Model):
    news_name = models.CharField(max_length=50)
    news_time = models.DateField(auto_now=False,auto_now_add=False)
    news_url = models.URLField(null=True,blank=True,max_length=50)
    news_source =  models.CharField(null=True,blank=True,max_length=30)

    content = models.TextField(null=True,blank=True)
	


    def __str__(self):
        return self.news_name
		
    class Meta:
        ordering = ['news_time']