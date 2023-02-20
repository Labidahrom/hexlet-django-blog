from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['who'] = 'World'
    #     return context

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
