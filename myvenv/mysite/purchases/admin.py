from django.contrib import admin
from .models import *

class PurchaseLineInline(admin.TabularInline):
    model = PurchaseLine
    extra = 10

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [
        PurchaseLineInline,
        ]

admin.site.register(Purchase, PurchaseAdmin)
