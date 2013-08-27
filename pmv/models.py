# Shawn Jain
# 8/20/2013
# PriceMyVet

from django.db import models

class Status_Type (models.Model):
	Status_Desc = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Service_Type (models.Model):
	Service_Type_desc = models.CharField(max_length=100)
	Add_Date = models.DateField(auto_now_add=True)

class Pet_Type (models.Model):
	Service_Type_desc = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Pet_Breed_Type (models.Model):
	Pet_Breed_Type_Desc = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Owner_Type (models.Model):
	Owner_Type = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Location_Type (models.Model):
	Location_Type = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Contact_Type (models.Model):
	Contact_Type = models.CharField(max_length=30)
	Add_Date = models.DateField(auto_now_add=True)

class Customer (models.Model):
	First_Name = models.CharField(max_length=50)
	Middle_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	Sex = models.CharField(max_length=10)
	Address = models.CharField(max_length=30)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Zip = models.CharField(max_length=15)
	Email_addr = models.EmailField()
	User_Name = models.CharField(max_length=150)
	Password = models.CharField(max_length=50)
	Add_Date = models.DateField(auto_now_add=True)

class Practice (models.Model):
	Practice_Name = models.CharField(max_length=50)
	Contact_First_Name = models.CharField(max_length=50)
	Contact_Middle_Name = models.CharField(max_length=50)
	Contact_Last_Name = models.CharField(max_length=50)
	Practice_Address = models.CharField(max_length=30)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=20)
	Zip = models.CharField(max_length=15)
	Country = models.CharField(max_length=50) 
	SSN_or_Tax_id =  models.CharField(max_length=20)
	Status_Type = models.ForeignKey(Status_Type)
	Parent_Practice_Ind = models.CharField(max_length=1)
	Practice_Profile = models.CharField(max_length=255)
	Practice_Photo = models.CharField(max_length=100)
	email_addr = models.EmailField() 
	web_site = models.URLField() 
	User_Name = models.CharField(max_length=150)
	Password = models.CharField(max_length=50)
	Add_Date = models.DateField(auto_now_add=True)

class Pet (models.Model):
	customer = models.ForeignKey(Customer)
	Pet_Name = models.CharField(max_length=50)
	Sex = models.CharField(max_length=10)
	Pet_Type = models.ForeignKey(Pet_Type)
	Pet_Breed_Type =  models.ForeignKey(Pet_Breed_Type)
	Pet_Age = models.CharField(max_length=5)
	Pet_Weight = models.CharField(max_length=5)
	Profile = models.CharField(max_length=255)
	Add_Date = models.DateField(auto_now_add=True)

class Vet (models.Model):
	First_Name = models.CharField(max_length=50)
	Middle_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	Sex = models.CharField(max_length=10)
	Address = models.CharField(max_length=30)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Zip = models.CharField(max_length=15)
	Profile = models.CharField(max_length=255)
	Licens_Number = models.CharField(max_length=30)
	Exp_No_of_Yr = models.CharField(max_length=5)
	Vet_Profile = models.CharField(max_length=255)
	Email_addr = models.EmailField() 
	Status_Type =  models.ForeignKey(Status_Type)
	Add_Date = models.DateField(auto_now_add=True)

class Search (models.Model):
	Search_Date = models.DateField(auto_now_add=True)
	Pet_Type = models.ForeignKey(Pet_Type)
	Service_Type = models.ForeignKey(Service_Type)
	search_Zip_Code = models.CharField(max_length=15)
	Radius = models.CharField(max_length=5)

class Practice_Vet (models.Model):
	Practice = models.ForeignKey(Practice)
	Vet = models.ForeignKey(Vet)
	Status_Type = models.ForeignKey(Status_Type)
	Add_Date = models.DateField(auto_now_add=True)

class Practice_Parent_Child (models.Model):
	Parent_Practice = models.ForeignKey(Practice)
	Child_Practice = models.ForeignKey(Practice, related_name='Child_Practice')
	Status_Type = models.ForeignKey(Status_Type)
	Add_Date = models.DateField(auto_now_add=True)

class Search_result (models.Model):
	search = models.ForeignKey(Search)
	Search_Result_Date = models.DateField(auto_now_add=True)
	Practice = models.ForeignKey(Practice)

class Phone (models.Model):
	Owner_Id = models.CharField(max_length=15)
	Owner_Type = models.ForeignKey(Owner_Type)
	Location_Type = models.ForeignKey(Location_Type)
	Contact_Type = models.ForeignKey(Contact_Type)
	Phone_Number = models.CharField(max_length=20)
	Add_Date = models.DateField(auto_now_add=True)

class Deal (models.Model):
	Customer = models.ForeignKey(Customer)
	Practice = models.ForeignKey(Practice)
	Service_Type = models.ForeignKey(Service_Type) 
	Pet_Type = models.ForeignKey(Pet_Type)
	Zip_code = models.CharField(max_length=15)
	Radius = models.CharField(max_length=5)
	Price = models.CharField(max_length=15)
	Status_Type = models.ForeignKey(Status_Type)
	Assign_date =  models.DateField(auto_now_add=True)
	Add_Date = models.DateField(auto_now_add=True)