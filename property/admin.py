from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat_in_owner.through
    raw_id_fields = ('flat', 'owner')
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'number_flat', 'like')


admin.site.register(Complaint, ComplaintAdmin)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat_in_owner',)
    list_display = ['full_name', 'owner_pure_phone_number']
    inlines = [OwnerInline]
