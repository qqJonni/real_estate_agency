from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'number_flat', 'like')


admin.site.register(Complaint, ComplaintAdmin)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat_in_owner',)
    list_display = ['full_name', 'owner_pure_phone_number']