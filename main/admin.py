from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Contact

admin.site.unregister(Group)
admin.site.unregister(User)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['first_name', 'last_name', 'phone_number', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone_number']

admin.site.register(Contact, ContactAdmin)