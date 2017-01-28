from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import NewsArticle

# Create your views here.

def index(request):
    all_articles_result = NewsArticle.objects.all()

    context = {}
    context['all_articles'] = all_articles_result

    return render(request, 'news/index.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    return render(request, 'news/detail.html', {'article' : article})
