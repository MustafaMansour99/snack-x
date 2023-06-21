from django.db import models
# from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model



# Create your models here.
class Snack(models.Model):
    name= models.CharField(max_length=255, null=False, blank=True)
    # purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    pur2=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])