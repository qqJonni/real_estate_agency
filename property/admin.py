from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ['full_name', 'pure_phone']
    inlines = [OwnerInline]
