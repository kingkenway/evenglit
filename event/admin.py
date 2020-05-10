from django.contrib import admin
from .models import Event, EventType

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'image',
                     'ticket_type', 'location', 'organiser_id',
                     'is_active', 'start_time', 'publish', 'created', 'updated',)
    list_filter = ('is_active', 'ticket_type', 'publish', 'organiser_id')
    ordering = ('title', 'is_active')
    search_fields = ('title', 'body')
    ordering = ('title', 'location')

    # raw_id_fields = ('organiser_id',)
    

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


# @admin.register(Event)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'publish', 'status')
#     list_filter = ('status', 'created', 'publish', 'author')
#     search_fields = ('title', 'body')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'publish'
#     ordering = ('status', 'publish')