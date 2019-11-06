from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from surveys.models import Snipp
from django.urls import reverse_lazy
#from django.contrib.auth.models import User
from django.contrib import admin,messages
from django.contrib.auth.models import User
#from django.contrib.admin import user
# 	from surveys.models import Request
#from django import forms
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.views.generic import TemplateView
from surveys.forms import SnippetForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags





def home(request):
	return render(request, 'surveys/home.html')	 
def status(request):
	if request.user.is_staff :
		response = redirect('staff_dashboard-page')
	else:
		response = redirect('student_dashboard-page')
	return response	
def login(request):
	if request.user.is_authenticated():
		response= redirect('student_dashboard-page')
	else:
		response= redirect('login-page')
	return response
	#return render(request, 'surveys/login.html')

def staff_dashboard(request):
	return render(request, 'surveys/dash/dashboard_home.html')

def staff(request):
	form=SnippetForm()
	posts=Snipp.objects.all()

	#print(posts)
	#obj = Snippet.objects.get(id=16)
	#context = {
	#'FirstName':obj.FirstName,
	#'LastName':obj.LastName,
	#'BITSID':obj.BITSID,
	#'Reason':obj.Reason

	#}
	args={'form':form,'posts':posts}
	return render(request, 'surveys/dash/dashboard.html',args)
@login_required
def stdashboard(request):
	return render(request, 'surveys/dash/student_dashboard.html')
@login_required
def student(request):
	

	if request.method == 'POST':
		
		form = SnippetForm(request.POST)
		if form.is_valid():

			FirstName=form.cleaned_data['FirstName']
			LastName=form.cleaned_data['LastName']
			Lecture1=form.cleaned_data['Lecture1']
			Lecture2=form.cleaned_data['Lecture2']
			BITSID=form.cleaned_data['BITSID']
			Reason=form.cleaned_data['Reason']
			Email=form.cleaned_data['Email']
			RequestDate=form.cleaned_data['RequestDate']
			ReturnDate=form.cleaned_data['ReturnDate']
			Address=form.cleaned_data['Address']
			form.save()
			print(ReturnDate+RequestDate)
			messages.success(request, 'Your Request has been forwarded successfully')
			html_message = render_to_string('status.html', {'context': "FirstName"})
			plain_message = strip_tags(html_message)
			
			if Lecture1=='s':
				send_mail('Request Form',plain_message,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],html_message=html_message,fail_silently=False)
				
			"""
			elif Lecture1=='p':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif Lecture1=='sa':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif Lecture1=='k':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)

			if Lecture2=='s':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif Lecture2=='p':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif Lecture2=='sa':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif Lecture2=='k':
				send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
		"""

		else:
			form = SnippetForm()
	form = SnippetForm()
	return render(request, 'surveys/dash/studentoriginal.html',{'form':form})
#def delete_new(request):

	#print(posts)
	#obj = Snippet.objects.get(id=16)
	#context = {
	#'FirstName':obj.FirstName,
	#'LastName':obj.LastName,
	#'BITSID':obj.BITSID,
	#'Reason':obj.Reason

	#}

	   #+some code to check if New belongs to logged in user
    #u = post.objects.get(pk=id).delete()
    #form=SnippetForm()
    #posts=Snippet.objects.all()
    #args={'form':form,'posts':posts}

    #return render(request, 'surveys/dash/dashboard.html')


"""

def delete_new(request, new_id):
    new_to_delete = get_object_or_404(New, id=new_id)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = DeleteNewForm(request.POST, instance=new_to_delete)

        if form.is_valid(): # checks CSRF
            new_to_delete.delete()
            return HttpResponseRedirect("/") # wherever to go after deleting

    else:
        form = DeleteNewForm(instance=new_to_delete)

    template_vars = {'form': form}
    return render(request, 'surveys/dash/dashboard.html', template_vars)
"""

class deleteview(DeleteView):
	model = Snipp
	success_url = reverse_lazy('staff-page')
	def test_func(self):
		post = self.get_object()                     
		return False
        #return(reverse('staff-page'))

"""	
template_name='surveys/dash/dashboard.html'
	def get_object(self):
		id_=self.kwargs.get("id")
		return get_object_or_404(posts,id=id_)

	def get_success_url(self):
		return reverse('staff-page')


def deleteview(request,pk):
	template_name='surveys/dash/dashboard.html'
	posts=get_object_or_404(Snippet,pk=pk)
	if request.method=="POST":


#return render(request, 'surveys/dash/dashboard.html')

	form = RequestForm(request.POST)
	if request.method == 'POST':
		form = RequestForm(request.POST)
		FirstName = request.POST.get("FirstName")
		LastName = request.POST.get("LastName")
		BITSID = request.POST.get("BITSID")
		Address = request.POST.get("Address")
		Email = request.POST.get("Email")
		MobileNum = request.POST.get("MobileNum")
		Reason = request.POST.get("Reason")
		Lecture1 = request.POST.get("Lecture1")
		Lecture2 = request.POST.get("Lecture2")
		send_mail('Request Form',FirstName,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)

		if form.is_valid():
			form.save()
			FirstName = form.cleaned_data.get('FirstName')
			LastName = form.cleaned_data.get('LastName')
			BITSID = form.cleaned_data.get('BITSID')
			Address = form.cleaned_data.get('Address')
			Email = form.cleaned_data.get('Email')
			MobileNum = form.cleaned_data.get('MobileNum')
			Reason = form.cleaned_data.get('Reason')
			Lecture1 = form.cleaned_data.get('Lecture1')
			Lecture2 = form.cleaned_data.get('Lecture2')
			return redirect('student-page')
	return render(request, 'surveys/dash/student.html',{'form':form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})






class student(LoginRequiredMixin,TemplateView):
	template_name = 'surveys/dash/student.html'
	def get(self,request):
		form = RequestForm()
		return render(request,self.template_name,{'form':form})
	def Request(self,request):
		form = RequestForm(request.POST)
		if form.is_valid():
			Request=form.save(commit=False)
			Request.User = request.User
			Request.save()
			FirstName = form.cleaned_data['FirstName']
			LastName = form.cleaned_data['LastName']
			BITSID = form.cleaned_data['BITSID']
			Address = form.cleaned_data['Address']
			Email = form.cleaned_data['Email']
			MobileNum = form.cleaned_data['MobileNum']
			Reason = form.cleaned_data['Reason']
			Lecture1 = form.cleaned_data['Lecture1']
			Lecture2 = form.cleaned_data['Lecture2']
			form=RequestForm()
			return redirect('student-page') 
		args={'form':form,'text':text}
		return render(request, self.template_name,args)




		#if(Lecture2>0):
		#	if(Lecture2==1):
		#			send_mail('Request Form',message,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
		

		
		
	#return render(request, 'surveys/dash/student.html',{'form':form, })


			FirstName = request.POST.get("FirstName")
			LastName = request.POST.get("LastName")
			BITSID = request.POST.get("BITSID")
			Address = request.POST.get("Address")
			Email = request.POST.get("Email")
			MobileNum = request.POST.get("MobileNum")
			Reason = request.POST.get("Reason")
			Lecture1 = request.POST.get("Lecture1")
			Lecture2 = request.POST.get("Lecture2")
			Request_obj = Request(FirstName=FirstName,LastName=LastName,BITSID=BITSID,Address=Address,Email=Email,MobileNum=MobileNum,Reason=Reason,Lecture1=Lecture1,Lecture2=Lecture2)
			Request_obj.save()
			print(FirstName,LastName,BITSID,Address,Email,MobileNum,Reason,Lecture2,Lecture1)
			message = FirstName+BITSID+Reason
						if(Lecture1 == '1'):
				print('its done')
				send_mail('Request Form',message,settings.EMAIL_HOST_USER,['sreenumalae@gmail.com'],fail_silently=False)
			elif(Lecture1== '2'):
				send_mail('Request Form',message,settings.EMAIL_HOST_USER,['anamprudhvikumarreddy@gmail.com'],fail_silently=False)

"""
