from django.contrib import admin
from .models import Info
from .models import predict

# Register your models here.

admin.site.register(Info)
admin.site.register(predict)