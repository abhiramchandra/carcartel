from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','car_title','city','created_date')
    list_display_links=('id','first_name','last_name')
    search_fields=('first_name','last_name','email','car_title')
admin.site.register(Contact,ContactAdmin)