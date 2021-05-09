from django.contrib import admin
import models

admin.site.register(models.Career)
admin.site.register(models.DefaultThing)
admin.site.register(models.UserInform)
admin.site.register(models.PhotoAnalysis)
admin.site.register(models.Diary)
admin.site.register(models.UserThings)
admin.site.register(models.DefaultNote)
admin.site.register(models.InstantPhotoAnalysis)


class Career(admin.ModelAdmin):
    list_display = ('career_id', 'career_name')
