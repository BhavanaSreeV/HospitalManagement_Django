from django.shortcuts import render,redirect
from .models import Doctors,Patients
from django.http import HttpResponse
from restaurent_project import settings
from .forms import Docform,patients_form,docupForm
from django.core.mail import EmailMessage
# Create your views here.

def hme(request):
	return render(request,'firstapp/home.html')

def btbl(request):
	return render(request,'firstapp/booking.html')
def login(request):
	return render(request,'firstapp/login.html')
def mnu(request):
	return render(request,'firstapp/menu.html')
def abt(request):
	return render(request,'firstapp/about.html')
def rgstr(request):
	return render(request,'firstapp/register.html')
def cnct(request):
	if request.method == "POST":
		name=request.POST['nm']
		sbj = request.POST['sb']
		m = request.POST['msg']
		sndr = request.POST['sn']
		email=EmailMessage(
			subject=sbj,
            body=f"Name: {name}\nEmail:{sndr}\nMessage: {m}",
            to=['bhavanasrivemuri@gmail.com'],
			)
		try:
			email.send()
		except:
			pass
	return render(request,'firstapp/contact.html')
def profile(request):
	k = Doctors.objects.all()
	if request.method == "POST":
		c = Docform(request.POST)
		if c.is_valid():
			c.save()
			return redirect('/prf')
	c = Docform()
	return render(request,'firstapp/profiles.html',{'w':c,'n':k})
def updt_dct(request,s):
	t = Doctors.objects.get(id=s)
	if request.method == "POST":
		z = docupForm(request.POST,instance=t)
		if z.is_valid():
			z.save()
			return redirect('/')
	z = docupForm(instance=t)
	return render(request,'firstapp/docupdate.html',{'h':z})
def docdlt(request,p):
	n = Doctors.objects.get(id=p)
	if request.method == "POST":
		n.delete()
		return redirect('/')
	return render(request,'firstapp/docdelete.html',{'z':n})


def cardio(request):
    d = Doctors.objects.filter(branch='1') 
    return render(request, 'firstapp/cardiology.html', {'f':d})

def neuro(request):
	d = Doctors.objects.filter(branch='3')
	print(d)
	return render(request,'firstapp/Neurology.html',{'f':d})
def gastro(request):
	d = Doctors.objects.filter(branch='4')
	return render(request,'firstapp/Gasterology.html',{'f':d})
def gynaco(request):
	d = Doctors.objects.filter(branch='5')
	return render(request,'firstapp/gynacology.html',{'f':d})
def dermo(request):
	d = Doctors.objects.filter(branch='2')
	return render(request,'firstapp/Dermatology.html',{'f':d})


def book(request):
    h = Patients.objects.all()
    if request.method == "POST":
        p = patients_form(request.POST)
        if p.is_valid():
            p.save()
            return redirect('/bt')
    p = patients_form() 

    return render(request, 'firstapp/book.html', {'b': p, 'n': h})


