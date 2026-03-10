from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ProfileTag, Purchase, Event, EventRegistration


class ProfileTagInline(admin.TabularInline):
    model = ProfileTag
    extra = 1


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'nickname', 'card_number', 'bonus_points']
    inlines = [ProfileTagInline]
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Пекарня', {'fields': ('nickname', 'card_number', 'date_of_birth', 'photo', 'bio', 'bonus_points')}),
    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'date']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'event']
