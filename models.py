from django.db import models
from django.utils import timezone

class Doctors(models.Model):
	g = [
		('0','Select Your Designation'),
		('1','CARDLGY'),
		('2','DERMA'),
		('3','NEURO'),
		('4','GASTRO'),
		('5','GYNECO'),
	]
	Doc_roll = models.CharField(max_length=15)
	doc_name = models.CharField(max_length=30)
	yearjoin = models.IntegerField(default='1')
	branch = models.CharField(max_length=20,choices=g,default=0)
	Phone=models.CharField(max_length=20,null=True)
	age = models.IntegerField(null=True)
	def __str__(self):
		return self.Doc_roll
	
class Doctor_updt(models.Model):
	g = [
		('0','Select Your Designation'),
		('1','CARDLGY'),
		('2','DERMA'),
		('3','NEURO'),
		('4','GASTRO'),
		('5','GYNECO'),
	]
	Doc_roll = models.CharField(max_length=15)
	doc_name = models.CharField(max_length=30)
	yearjoin = models.IntegerField(default='1')
	branch = models.CharField(max_length=15,choices=g,default=0)
	Phone=models.CharField(max_length=20,null=True)
	age = models.IntegerField(null=True)


