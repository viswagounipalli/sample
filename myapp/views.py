from django.shortcuts import render,redirect
from myapp.forms import register_form,login_form
from myapp.models import register
from django.http import HttpResponse
import random
def Home(request):
	return render(request,"home.html")

def Register_fun(request):
	if request.method=="POST":
		register_f=register_form(request.POST)
		if register_f.is_valid():
			register_f.save()			
			request.session["uname"]=register_f.cleaned_data["firstname"]
			f_data=register.objects.filter(firstname=register_f.cleaned_data["firstname"],email=register_f.cleaned_data["email"])
			return render(request,"user_inforamation_page.html",{"data":f_data})
	else:
		register_f=register_form()
		return render(request,"register_page.html",{"data":register_f})

def login_fun(request):
	if request.method=="POST":
		login_data=register.objects.filter(firstname=request.POST["username"],password=request.POST["password"])
		if login_data:			
			request.session["uname"]=request.POST["username"]
			return redirect("userdashboard")
		#return render(request,"user_inforamation_page.html",{"data":data})
		else:
			#login_f=login_form()
#			wrong_credentails.html
			return render(request,"wrong_credentails.html",{"data":" "})
	else:
		login_f=login_form()
		return render(request,"login_page.html",{"data":login_f})
		#return render(request,"wrong_credentails.html",{"data":"Username and password Incorrect"})
def update_fun(request,id):
	data=register.objects.get(id=id)
	form = register_form(request.POST or None,instance=data)
	if form.is_valid():
		form.save(commit=True)
		request.session["uname"]=form.cleaned_data["firstname"]
	#	f_data=register.objects.filter(firstname=form.cleaned_data["firstname"],email=form.cleaned_data["email"])
		return redirect("userdashboard")
	else:
		return render(request,"update_page.html",{"data":form})
	
def user_dashboard(request):
	if request.session.has_key("uname"):
		data_list=register.objects.filter(firstname=request.session["uname"])
		return render(request,"user_inforamation_page.html",{"data":data_list})
	else:
		return redirect("home")

def logout_fun(request):
	del request.session["uname"]
	return redirect("home")


def delete_fun(request,id):
	if request.session.has_key("uname"):
		del request.session["uname"]
		obj=register.objects.get(id=id)
		obj.delete()
		return redirect("userdashboard")
	else:
		return redirect("home")


def aboutus_fun(request):
	return render(request,"aboutus.html",{"data":" "})

def contactus_fun(request):
	return render(request,"contactus.html",{"data":" "})




