from django.db import models

# Create your models here.


class PhotoAnalysis(models.Model):
    photo_id = models.AutoField(primary_key=True)
    line_id = models.CharField(max_length=120, blank=False, null=False)
    date = models.DateTimeField()
    pic = models.ImageField(upload_to='images')
