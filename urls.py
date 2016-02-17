from django.conf.urls import include, url
from django.contrib import admin
from views import index

urlpatterns = [
    url(r'^articles/', include('articles.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^edit/', include('edit.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
