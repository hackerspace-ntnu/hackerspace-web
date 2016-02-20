from django.contrib import admin
from textboxes.models import Textbox


@admin.register(Textbox)
class TextboxAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Textbox', {
            'fields': [
                'title',
                'content'
            ]
        }),
        (None, {
            'fields': [
                'pub_date'
            ]
        }),
    ]
    search_fields = ['title']
