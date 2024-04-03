from django.contrib import admin
from Crudassignment.models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_Display = ("id","ename","elocation","email")

admin.site.register(Emp,EmpAdmin)
# Register your models here.
