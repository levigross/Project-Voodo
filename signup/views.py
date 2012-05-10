from django.shortcuts import render_to_response, redirect
from forms import SignupForm
from django.template import RequestContext
from django.views.generic import CreateView, TemplateView
from models import Signup
from django.http import HttpResponseRedirect
from django.contrib import messages

class HomePage(TemplateView):
	template_name = "basesite/home.html"

class SiteSignup(CreateView):
	template_name= "signup/signup.html"
	form_class = SignupForm
	success_url = ""
	

	def post(self, request, *args, **kwargs):
		form=SignupForm(self.request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, "Thank you for signing up to Voodoo")
			return redirect('home_page')
		else:
			return self.render_to_response(self.get_context_data(form=form))
		messages.add_message(self.request, messages.INFO, message="Please eneter a valid information.")


	def get_context_data(self, **kwargs):
		context = super(SiteSignup, self).get_context_data(**kwargs)
		if self.request.POST:
			context['SignupForm'] = SignupForm(self.request.POST)
		else:
			context['SignupForm'] = SignupForm()
		return context




