from django.urls import path
from hexlet_django_blog.article.views import ArticlePageView
from hexlet_django_blog.article.views import ArticleView
from hexlet_django_blog.article.views import index
from hexlet_django_blog.article.views import ArticleFormCreateView
from hexlet_django_blog.article.views import ArticleFormEditView


urlpatterns = [
    path('', ArticlePageView.as_view()),
    path('<str:tag>/<int:article_id>/', index, name='article',),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create')

]
