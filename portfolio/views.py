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
    #initial = {'created_by': getattr(self.request, 'user', None)}

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, u"Project %s has been created" % self.object.title)
        super(CreateProject,self).get_success_url()


class UpdateProject(UpdateView):
    form_class = CreateProjectForm
    model = Project
    template_name = 'portfolio/user_update.html'
	
    def get_object(self, queryset=None):
        obj = User.objects.get(username=self.request.user)
        return obj
	
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteProject(DeleteView):
    model = Project


class ListView(TemplateView):
    template_name = 'portfolio/project_view.html'

    def get_context_data(self, **kwargs):
        return {
            'projects':Project.objects.all().order_by('pk'),
        }