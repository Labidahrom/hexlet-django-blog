from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    app_name = 'article'
    return render(request, 'article/index.html',
                  context={'app_name': app_name},)
