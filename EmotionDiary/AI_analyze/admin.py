from django.contrib import admin

# Register your models here.
from . import models
# from .models import Career

admin.site.register(models.Career)
admin.site.register(models.DefaultThing)
admin.site.register(models.UserInform)
admin.site.register(models.AnalysisDiary)
admin.site.register(models.Diary)
admin.site.register(models.UserThings)
admin.site.register(models.DefaultNote)

class Career(admin.ModelAdmin):
    list_display = ('career_id', 'career_name')
