# Create your views here.

from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from portfolio.models import Project

class ViewPortfolio(TemplateView):
    def get_context_data(self, **kwargs):
        template_name = 'portfolio/portfolio_view.html'

        return {
            'portfolio': get_object_or_404(Project.objects.get(public_id=kwargs.get('public_id'))),
            }



