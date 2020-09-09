from django.shortcuts import render
from . import models
# Create your views here.
def articles_list(request):
    article = models.Article.objects.all().order_by('date')
    args={'article':article}
    return render(request, 'articles/articleslist.html',args)