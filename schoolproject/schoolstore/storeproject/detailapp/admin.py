from django.contrib import admin

from detailapp.models import Course, ContactQuery

# Register your models here.
admin.site.register(Course)
admin.site.register(ContactQuery)