from django.db import models

# Create your models here.
class Career(models.Model):
    career_id = models.IntegerField(primary_key=True)
    career_name = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.career_name


class DefaultThing(models.Model):
    things_id = models.IntegerField(primary_key=True)
    things = models.CharField(max_length=10, blank=False, null=False)


class UserInform(models.Model):
    line_id = models.CharField(primary_key=True, max_length=120, blank=False, null=False)
    username = models.CharField(max_length=20, blank=False, null=False)
    gender = models.CharField(max_length=20, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    career_id = models.ForeignKey(Career, on_delete=models.CASCADE)


class PhotoAnalysis(models.Model):
    photo_id = models.AutoField(primary_key=True)
    line_id = models.CharField(max_length=120, blank=False, null=False)
    date = models.DateTimeField()
    pic = models.ImageField(upload_to='images')


class Diary(models.Model):
    line_id = models.ForeignKey(UserInform, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    mood = models.IntegerField(null=False)
    note = models.CharField(max_length=255)
    pic = models.ImageField(null=False)

    class Meta:
        unique_together = ("line_id", "date")


class UserThings(models.Model):
    id = models.AutoField(primary_key=True)
    line_id = models.ForeignKey(UserInform, on_delete=models.CASCADE)
    things_id = models.ForeignKey(DefaultThing, on_delete=models.CASCADE)
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)


class DefaultNote(models.Model):
    note_id = models.IntegerField(primary_key=True)
    default_note = models.CharField(max_length=255, blank=False, null=False)
