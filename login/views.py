from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect
from forms import LoginForm
from django.contrib import messages
from django.shortcuts import redirect


class HomeView(TemplateView):
	 template_name = 'home.html'

class SiteLogin(TemplateView):
	form_class = LoginForm
	template_name = 'login/login.html'
	success_url = ""
	
	def get_context_data(self, **kwargs):
		self.form_class()
		return {
            'form': LoginForm() if not kwargs.get('form') else kwargs['form'],
		}
		
	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			messages.add_message(self.request, messages.INFO, message="You have succesfully logged in")
			return redirect('home')
		else:
			return self.get(request, form=LoginForm)

	
	def login_validation(self,form):
		username = request.POST['username']
		pw = request.POST['password']
		user = authentication(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('')
			else:
				return self.render_to_response(self.get_context_data(form=form))
			messages.add_message(self.request, messages.INFO, message="Username or password does not exist")
		else:
			return self.render_to_response(self.get_context_data(form=form)) 
			messages.add_message(self.request, messages.INFO, message="Please enter a valid username and password")
			