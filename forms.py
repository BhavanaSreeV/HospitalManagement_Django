from .models import Doctors,Patients,Doctor_updt
from django import forms

class Docform(forms.ModelForm):
	class Meta:
		model = Doctors
		fields = ['Doc_roll','doc_name','branch','yearjoin','age','Phone']
		widgets = {
		"Doc_roll":forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':'Enter Doctor_ID',
			}),
		"doc_name":forms.TextInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Doc_Name",
			}),
		"branch":forms.Select(attrs={
			'class':"form-control my-1",
			}),
		"yearjoin":forms.NumberInput(attrs={
            'class': "form-control my-1",
			'placeholder':"Enter YearJoin",
			}),
		
		"age":forms.NumberInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Age",
			}),
		"Phone":forms.NumberInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Contact Number",
			}),
		}

class docupForm(forms.ModelForm):
	class Meta:
		model = Doctor_updt
		fields = ['Doc_roll','doc_name','branch','yearjoin','age','Phone']
		widgets = {
		"Doc_roll":forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':'Enter Doctor_ID',
			}),
		"doc_name":forms.TextInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Doc_Name",
			}),
		"branch":forms.Select(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Branch",
			}),
		"yearjoin":forms.NumberInput(attrs={
            'class': "form-control my-1",
			'placeholder':"Enter YearJoin",
			}),
		
		"age":forms.NumberInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Age",
			}),
		"Phone":forms.NumberInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Contact Number",
			}),
		}
