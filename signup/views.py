from django.shortcuts import render_to_response, redirect
from forms import SignupForm
from django.template import RequestContext
from django.views.generic import CreateView, TemplateView

class home(TemplateView):
	template_name = "home.html"

class signup(CreateView):
	template_name: "signup.html"
	model = Signup
	form_class = SignupForm
	success_url = ""

	def form_valid(request):
    	if request.method == 'POST':
       	 	form = SignupForm(request.POST)
        	if form.is_valid():
            	form.save()
            	messages.add_message(request, messages.INFO, "Thank you for signing up to Voodoo")
            	return redirect('')
   		 else:
    	    form = SignupForm()
    	return render_to_response('templates/signup/signup.html', {'form': form}, context_instance=RequestContext(request))

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
		
	def get_context_data(self, **kwargs):
		context = super(signup, self).get_context_data(**kwargs)
		if self.request.POST:
			context['SignupForm'] = SignupForm(self.request.POST)
		else:
			context['SignupForm'] = SignupForm()
		return context