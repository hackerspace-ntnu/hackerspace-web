from django.shortcuts import render
from articles.models import Article, Thumbnail
from events.models import Event
from events.models import Thumbnail as EventThumbnail
from textboxes.models import Textbox
from login.models import LoginForm


def index(request):
    event_list = Event.objects.order_by('-date')
    article_list = Article.objects.order_by('-pub_date')[:3]
    thumbnail_list = Thumbnail.objects.all()
    event_thumbnail_list = EventThumbnail.objects.all()
    textbox_list = Textbox.objects.order_by('-pub_date')
    form = LoginForm()
    context = {
        'article_list': article_list,
        'thumbnail_list': thumbnail_list,
        'event_list': event_list,
        'event_thumbnail_list': event_thumbnail_list,
        'textbox_list': textbox_list,
        'form': form
    }

    return render(request, 'index.html', context)
