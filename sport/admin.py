from django.contrib import admin
from .models import *


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Teams)
admin.site.register(Games)
admin.site.register(Order)

