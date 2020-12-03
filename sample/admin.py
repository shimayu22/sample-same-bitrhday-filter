from django.contrib import admin

# Register your models here.
from sample.models import Samplepeople

class SamplepeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'kana', 'date_of_birth')

admin.site.register(Samplepeople, SamplepeopleAdmin)
