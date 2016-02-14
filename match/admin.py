from django.contrib import admin
from .models import (Match, Item)

class ItemInline(admin.TabularInline):
    model = Item

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
