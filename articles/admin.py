from django.contrib import admin
from articles.models import Article, Thumbnail


class ThumbnailInline(admin.StackedInline):
    model = Thumbnail
    max_num = 1
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
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
        (None, {
            'fields': [
                'pub_date'
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
