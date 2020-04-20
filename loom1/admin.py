from django.contrib import admin
from .models import PrimaryTable,FaultTable,MasterTable

# Register your models here.
admin.site.register(PrimaryTable)
admin.site.register(MasterTable)
admin.site.register(FaultTable)

