from django.shortcuts import render
from django.http import HttpResponseRedirect
from edit.models import EventEditForm, ArticleEditForm
from events.models import Event
from articles.models import Article


def event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventEditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            event_id = form.cleaned_data['event_id']
            event = Event.objects.get(pk = event_id)
            event.ingress_content = form.cleaned_data['ingress_content']
            event.main_content = form.cleaned_data['main_content']
            event.save()
            return HttpResponseRedirect('/events/'+str(event_id)+'/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventEditForm()

    return render(request, 'edit_event.html', {'form': form})

def article(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleEditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            article_id = form.cleaned_data['article_id']
            article = Article.objects.get(pk = article_id)
            article.ingress_content = form.cleaned_data['ingress_content']
            article.main_content = form.cleaned_data['main_content']
            article.save()
            return HttpResponseRedirect('/articles/'+str(article_id)+'/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleEditForm()

    return render(request, 'edit_article.html', {'form': form})