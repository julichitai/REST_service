from django.contrib import admin
from Message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('messageText',)


admin.site.register(Message, MessageAdmin)
