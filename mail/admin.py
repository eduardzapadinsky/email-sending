from django.contrib import admin

from mail.models import ContactBase


@admin.register(ContactBase)
class ContactBaseAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
