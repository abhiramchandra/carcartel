from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnall(self,object):
        return format_html('<img src="{}" width="40" style="broder-radius:50px;"/>'.format(object.photo.url))
    thumbnall.short_description='photo'
    list_display=('id','thumbnall','first_name','designation','created_date')
    list_display_links=('id','thumbnall','first_name',)
    search_fields=('first_name','last_name','designation')
    list_filter=('designation',)

admin.site.register(Team,TeamAdmin)
