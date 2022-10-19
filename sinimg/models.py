from django.db import models

# Create your models here.
class SinImg(models.Model):
    img = models.ImageField(upload_to="images/single")

    def __str__(self):
        return f"#{self.id} {self.img.name.split('/')[-1]}"