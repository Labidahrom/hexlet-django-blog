
from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views
from hexlet_django_blog.views import HomePageView



urlpatterns = [
    path('', HomePageView.as_view(template_name='index.html')),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('article/', include('hexlet_django_blog.article.urls')),
]

