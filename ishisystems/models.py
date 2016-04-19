"""ishissystems website models"""
from django.db import models
from datetime import datetime  
from django.db.models.fields.related import ForeignKey
from django.contrib.admin.utils import help_text_for_field

# Create your models here.
# Question Table Model
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_when=models.DateTimeField()
    modified_when=models.DateTimeField()

    def __str__(self):
        return self.full_name
        
 
# People Table Model
class People(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,help_text="Currently not displayed on site") 
    img_path = models.CharField(max_length=255,help_text="relative path of people image like images/peoples/xyz.jpg, peoples images should be in images/peoples/ folder")
    position = models.CharField(max_length=30,blank=True,help_text="Currently not displayed on site") 
    created_when=models.DateTimeField()
    modified_when=models.DateTimeField()
    
    def __str__(self):
        return self.first_name 
#Job Table Model
class Job(models.Model): 
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=30,help_text="Country name like USA,India,Switzerland") 
    city = models.CharField(max_length=30)
    position = models.CharField(max_length=30) 
    type = models.CharField(max_length=30,blank=True,help_text="Type is Fulltime or Parttime") 
    skills_set = models.CharField(max_length=255,blank=True)  
    compensation = models.CharField(max_length=30,blank=True,help_text="Its value is DOE") 
    job_detail_page = models.CharField(max_length=50,blank=True,help_text="relative path of the job detail html page like /content/jobs/sr_devops_engineer.html.Create a template for job description and put in /content/jobs/ folder.")
    created_when=models.DateTimeField()
    modified_when=models.DateTimeField()
    
    def __str__(self):
        return self.position 

 
     
#Client Table Model
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,help_text="Client Name")
    img_path = models.CharField(max_length=255,help_text="relative path of client logo image like images/clients/marsh.jpg, client image should be in images/clients/ folder")
    description = models.TextField(blank=True,help_text="Description about client.Not displayed on site currently") 
    created_when=models.DateTimeField()
    modified_when=models.DateTimeField()
    
    def __str__(self):
        return self.name 
    
#Contact Us Table Model  
class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255,blank=True)
    email = models.EmailField() 
    phone_no = models.CharField(max_length=100,blank=True) 
    note = models.TextField()
    created_when=models.DateTimeField()
    modified_when=models.DateTimeField()
    
    def __str__(self):
        return self.full_name  

 
    