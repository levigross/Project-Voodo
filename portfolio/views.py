# Create your views here.

from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from portfolio.models import Project
from portfolio.forms import CreateProjectForm

class ViewProject(TemplateView):

    template_name = 'portfolio/project_view.html'

    def get_context_data(self, **kwargs):
        return {
            'portfolio': get_object_or_404(Project.objects.get(public_id=kwargs.get('public_id'),
                slug=kwargs.get('slug'))),
            }



class CreateProject(CreateView):
    success_url = 'portfolio_update'
    form_class = CreateProjectForm
    template_name = 'portfolio/create_project.html'
    initial = {'created_by': getattr(self.request, 'user', None)}

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, u"Project %s has been created" % self.object.title)
        super(self, CreateProject).get_success_url()



class UpdateProject(UpdateView):
    pass
