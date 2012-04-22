from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect
from forms import LoginForm



class home(TemplateView):
	 template_name = 'home'

class siteLogin(CreateView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = ""
	
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
			