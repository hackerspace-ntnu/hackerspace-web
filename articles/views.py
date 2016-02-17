from django.shortcuts import render
from articles.models import Article, Thumbnail
from edit.models import ArticleEditForm
from django import forms


def index(request):
    article_list = Article.objects.order_by('-pub_date')
    thumbnail_list = Thumbnail.objects.all()
    context = {
        'article_list': article_list,
        'thumbnail_list': thumbnail_list
    }

    return render(request, 'articles.html', context)


def article(request, article_id):
    requested_article = Article.objects.get(pk=article_id)
    form = ArticleEditForm(initial={
        'article_id': article_id,
        'ingress_content': requested_article.ingress_content,
        'main_content': requested_article.main_content
    })
    form.fields['article_id'].widget = forms.HiddenInput()
    context = {
        'article': requested_article,
        'form': form,
    }

    return render(request, 'article.html', context)