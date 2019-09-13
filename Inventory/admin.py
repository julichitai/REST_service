from django.contrib import admin
from Inventory.models import ItemType, Item


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemType',)


admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
