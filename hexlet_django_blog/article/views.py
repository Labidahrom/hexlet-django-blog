from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from hexlet_django_blog.views import HomePageView
from django.views import View
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class ArticlePageView(HomePageView):
    template_name = "article/index.html"

    def get_context_data(self, **kwargs):
        app_name = 'article'
        context = super().get_context_data(**kwargs)
        context['app_name'] = app_name
        return context

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


def index(request, tag, article_id):
    return render(request, 'article/id.html', context={
        'tag': tag, 'article_id': article_id,
    })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('/')  # Редирект на указанный маршрут
        # Если данные некоректные, то возвращем человека обратно на страницу с заполенной формой
        return render(request, 'article/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})