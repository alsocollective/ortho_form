# from django import forms
# from form.models import *

# class ApplicationForm(forms.Form):
# 	class Meta:
# 		models = Application
# 		fields = ['fullName',]


from django.forms import ModelForm
from form.models import *

class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['fullName','email','phone','statement','cv','portrait','reference_1','reference_2','reference_3',]
