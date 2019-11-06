from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django.contrib.auth.models import User
from .models import Snipp


class SnippetForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		self.helper = FormHelper
		self.helper.form_method = "POST"
		self.helper.layout = Layout(
			'FirstName',
			'LastName',
			'BITSID',
			'Reason',
			'Address',
			'Email',
			'RequestDate',
			'ReturnDate',
			'Lecture1',
			'Lecture2',
			Submit('submit','Submit',css_class="btn-success"))
	
	class Meta:
		model = Snipp
		fields = ['FirstName', 'LastName', 'BITSID','Address','Reason','Email','RequestDate','ReturnDate','Lecture1','Lecture2']
#
