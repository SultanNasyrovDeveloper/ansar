from django.contrib import admin
from .models import Callback


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    pass
