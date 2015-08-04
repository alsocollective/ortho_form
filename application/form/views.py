from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from form import models
from django.template.context_processors import csrf

from form import forms



# Create your views here.
def home(request):
	if request.method == 'POST':
		print "it's a submission"
		form = forms.ApplicationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/success/')
	else:
		form = forms.ApplicationForm()
	return render(request, 'register.html', {'form':form})

def success(request):
	return HttpResponse("it worked")
