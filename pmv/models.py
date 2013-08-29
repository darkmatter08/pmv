# Shawn Jain
# 8/28/2013
# PriceMyVet

from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField, USPostalCodeField
from django.contrib.auth.models import User

from datetime import date

###### SEX_CHOICES ######
MALE = 'M'
FEMALE = 'F'
SEX_CHOICES = [
	(MALE, 'Male'),
	(FEMALE, 'Female'),
]
###### 

class Address(models.Model):
	mobile_number = PhoneNumberField()
	home_number = PhoneNumberField()
	fax_number = PhoneNumberField()
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = USStateField()
	zip_code = USPostalCodeField()

class Licence(models.Model):
	id_number = models.CharField(max_length=30)
	expiration = models.DateField()
	state_of_issue = USStateField()

	def is_valid():
		if (expiration - date.today()).total_seconds() >= 0:
			return True
		else:
			return False

class Person(User):
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
	address = models.OneToOneField(Address)
	add_date = models.DateTimeField(auto_now_add=True)
	is_vet = models.BooleanField() #Want to remove this. 

	def save(self, *args, **kwargs):
		User.username = User.email
		User.save()
		super(Person, self).save(*args, **kwargs)

	class Meta:
		abstract = True

class Owner(Person):
	pass

class Vet(Person):
	profile = models.CharField(max_length=255)
	licence = models.OneToOneField(Licence)
	# TODO: Status type??

class Pet(models.Model):
	owner = models.ForeignKey(Owner)
	name = models.CharField(max_length=50)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES)
#	animal_type = models.ForeignKey(Animal_Type)
#	animal_breed = models.ForeignKey(Animal_Breed)

