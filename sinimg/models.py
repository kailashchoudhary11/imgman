from django.db import models
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField
from django.dispatch import receiver

# Create your models here.
class SinImg(models.Model):
    '''
    Creates an image model.
    '''
    img = CloudinaryField('image', folder="media/images/single")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} {self.img.public_id.rsplit('/')[-1]}"

@receiver(pre_delete, sender=SinImg)
def photo_delete(sender, instance, **kwargs):
    '''
    Deletes the image.
    '''
    cloudinary.uploader.destroy(instance.img.public_id)