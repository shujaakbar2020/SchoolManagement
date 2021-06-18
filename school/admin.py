from django.contrib import admin
from .models import Attendance, Notice, Marks

# Register your models here.

admin.site.register(Attendance)
admin.site.register(Notice)
admin.site.register(Marks)
