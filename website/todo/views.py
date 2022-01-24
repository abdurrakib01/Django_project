from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
class Homeview(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Abdur Rakib"
        context['country'] = "Bangladesh"
        list = [1,2,3,4,5]
        context['list'] = list
        return context
