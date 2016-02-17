from django.conf.urls import url

from edit import views

urlpatterns = [
    url(r'^article/', views.article, name='article'),
    url(r'^event/', views.event, name='event'),
]
