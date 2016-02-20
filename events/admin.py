from django.contrib import admin
from events.models import Event, Thumbnail


class ThumbnailInline(admin.StackedInline):
    model = Thumbnail
    max_num = 1
    extra = 0


@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    fieldsets = [
        ('Article', {
            'fields': [
                'title',
                'main_content'
            ]
        }),
        ('Ingress', {
            'fields': [
                'ingress_content'
            ]
        }),
        ('Dates', {
            'fields': [
                'pub_date',
                'date'
            ]
        }),
        ('Place', {
            'fields': [
                'place',
                'place_href'
            ]
        }),
        ('Thumbnail', {
            'fields': [
                'thumbnail',
            ]
        })
    ]
    search_fields = [
        'title'
    ]


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Thumbnail', {
            'fields': [
                'title',
                'image',
            ]
        })
    ]
    search_fields = [
        'title'
    ]
