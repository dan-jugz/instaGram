from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default='')
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    comments = models.CharField(max_length =1000, default="Not comments yet")
    likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()