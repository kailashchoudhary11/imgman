from django.db import models

# Create your models here.
class SinImg(models.Model):
    img = models.ImageField(upload_to="images/single")