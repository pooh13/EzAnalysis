from django.db import models

# Create your models here.
class Career(models.Model):
    career_id = models.IntegerField(primary_key=True)
    career_name = models.CharField(max_length=10, blank=False, null=False)

    def __unicode__(self):
        return self.career_id

class UserInform(models.Model):
    line_id = models.CharField(primary_key=True, max_length=120, blank=False, null=False)
    username = models.CharField(max_length=20, blank=False, null=False)
    gender = models.IntegerField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    career_id = models.ForeignKey(Career, on_delete=models.CASCADE)

class PhotoAnalysis(models.Model):
    photo_id = models.AutoField(primary_key=True)
    line_id = models.CharField(max_length=120, blank=False, null=False)
    date = models.DateTimeField()
    pic = models.ImageField(upload_to='images')
