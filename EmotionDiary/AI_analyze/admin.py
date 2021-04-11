from django.contrib import admin

# Register your models here.
from . import models
# from .models import Career

admin.site.register(models.Career)
admin.site.register(models.UserInform)
admin.site.register(models.PhotoAnalysis)

class Career(admin.ModelAdmin):
    list_display = ('career_id', 'career_name')
