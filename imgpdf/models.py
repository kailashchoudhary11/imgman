from django.db import models

# Create your models here.
class imgpdf:
    img = models.ImageField(null=True, blank=True, upload_to="images/")