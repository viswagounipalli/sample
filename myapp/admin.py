from django.contrib import admin

# Register your models here.
from myapp.models import register as register_table
admin.site.register(register_table)