# Create your tests here.
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from ishisystems.forms import QuestionForm
from ishisystems.forms import ContactForm
from django.utils import timezone
from ishisystemswebsite.ishisystems.models import Question, ContactUs
from ishisystemswebsite.ishisystems.models import ContactUs
from ishisystemswebsite.ishisystems.models import Job
#since our client model conflicts with test.client model that's why commenting it and its call also.
#from ishisystemswebsite.ishisystems.models import Client
from ishisystemswebsite.ishisystems.models import People
from ishisystemswebsite.ishisystems.views import question_response
from ishisystemswebsite.ishisystems.views import contact_response


#TestCases for views and Urls
class AppTestCases(TestCase):

    def setUp(self):
        self.c = Client()

    def index_access(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_capabilities_access(self): 
        response = self.c.get(reverse('capabilities'))
        self.assertEqual(response.status_code, 200) 
    
    def test_services_access(self): 
        response = self.c.get(reverse('services'))
        self.assertEqual(response.status_code, 200) 
    
    def test_clients_access(self): 
        response = self.c.get(reverse('clients'))
        self.assertEqual(response.status_code, 200) 
        
    def test_contactus_access(self): 
        response = self.c.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)  
    def test_question_response_access(self): 
        response = self.c.get(reverse('question_response'))
        self.assertEqual(response.status_code, 200)  

#Test Cases for Models of application
class QuestionModelTestCases(TestCase):
    def create_question(self, full_name="TestName",email="xyz@gmail.com" ,message="yes, this is only a test"):
        return Question.objects.create(full_name=full_name, email=email,message=message,created_when=timezone.now(),modified_when=timezone.now())

    def test_question_creation(self):
        q = self.create_question()
        self.assertTrue(isinstance(q, Question))
        self.assertEqual(q.__str__(), q.full_name)

class ContactModelTestCases(TestCase):
    def create_contact(self, full_name='',company_name="",email="xyz@gmail.com",phone_no='',note="yes, this is only a test"):
        return ContactUs.objects.create(full_name=full_name,company_name=company_name, email=email,phone_no=phone_no,note=note,created_when=timezone.now(),modified_when=timezone.now())

    def test_contact_creation(self):
        con = self.create_contact()
        self.assertTrue(isinstance(con, ContactUs))
        self.assertEqual(str(con), con.full_name)
class JobModelTestCases(TestCase):
    def create_job(self, country_name='USA',city="London",position="Engg",type='PartTime',skills_set="yes, this is only a test",compensation='DOE',job_detail_page="XYZ"):
        return Job.objects.create(country_name=country_name,city=city,position=position,type=type,skills_set=skills_set,compensation=compensation,job_detail_page=job_detail_page,created_when=timezone.now(),modified_when=timezone.now())

    def test_job_creation(self):
        job = self.create_job()
        self.assertTrue(isinstance(job, Job))
        self.assertEqual(str(job), job.position)
        
class PeopleModelTestCases(TestCase):
    def create_people(self, first_name='FirstTestName',last_name="TestName",img_path="xyz",position='xyz' ):
        return People.objects.create(first_name=first_name,last_name=last_name,img_path=img_path,position=position,created_when=timezone.now(),modified_when=timezone.now())

    def test_people_creation(self):
        p = self.create_people()
        self.assertTrue(isinstance(p, People))
        self.assertEqual(str(p), p.first_name)

#since our client model conflicts with test.client model that's why commenting it and its call also.
#from ishisystemswebsite.ishisystems.models import Client       
#===============================================================================
# class ClientModelTestCases(TestCase):
#     def create_client(self, name='TestName',img_path="xyz",description="xyz@gmail.com",):
#         return Client.objects.create(name=name,img_path=img_path,description=description,created_when=timezone.now(),modified_when=timezone.now())
# 
#     def test_client_creation(self):
#         cl = self.create_client()
#         self.assertTrue(isinstance(cl, Client))
#         self.assertEqual(str(cl), cl.name)
#         
#===============================================================================

#Test Cases for Question form         
class QuestionFormTestCases(TestCase):    
    def setUp(self):
        self.c = Client()
    def test_invalid_question_form(self):
        q = Question.objects.create(full_name="TestName",email="xyz@gmail.com" ,message="",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': q.full_name,'email':q.email,'message':q.message,'created_when':timezone.now(),'modified_when':timezone.now()} 
        form = QuestionForm(data=form_data)
        self.assertFalse(form.is_valid())
        
    def test_valid_question_form(self):
        q = Question.objects.create(full_name="TestName",email="xyz@gmail.com" ,message="Testing....",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': q.full_name,'email':q.email,'message':q.message,'created_when':timezone.now(),'modified_when':timezone.now()} 
        form = QuestionForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_entry_create(self): 
        """To  make this test work we need to uncomment the else part in views.question_response methods"""
        q = Question.objects.create(full_name="TestName",email="xyz@gmail.com" ,message="",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': q.full_name,'email':q.email,'message':q.message,'created_when':timezone.now(),'modified_when':timezone.now()}  
        response = self.c.post(reverse('question_response') , form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "message", "This field is required.")
        

    def test_valid_entry_create(self):  
        form_data = {'full_name':"TestName",'email':"xyz@gmail.com",'message':"Testing...",'created_when':timezone.now(),'modified_when':timezone.now()}  
        self.assertEqual(Question.objects.count(), 0)
        response = self.c.post(reverse('question_response') , form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.count(), 1)   

#Test Cases for Contact Form      
class ContactFormTestCases(TestCase):  
      
    def setUp(self):
        self.c = Client()
        
    def test_invalid_contact_form(self):
        con = ContactUs.objects.create(full_name='',company_name="",email="xyz@gmail.com",phone_no='',note="yes, this is only a test",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': con.full_name,'email':con.email,'note':con.note,'created_when':timezone.now(),'modified_when':timezone.now()} 
        form =ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        
    def test_valid_contact_form(self):
        con = ContactUs.objects.create(full_name='Test',company_name="",email="xyz@gmail.com",phone_no='',note="yes, this is only a test",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': con.full_name,'company_name':"",'email':con.email,'note':con.note,'created_when':timezone.now(),'modified_when':timezone.now()} 
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_entry_create(self): 
        """To  make this test work we need to uncomment the else part in views.contact_response methods"""
        con = ContactUs.objects.create(full_name='',company_name="",email="xyz@gmail.com",phone_no='',note="yes, this is only a test",created_when=timezone.now(),modified_when=timezone.now())
        form_data = {'full_name': con.full_name,'company_name':"",'email':con.email,'note':con.note,'created_when':timezone.now(),'modified_when':timezone.now()} 
        response = self.c.post(reverse('contact_response') , form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "full_name", "This field is required.")
        

    def test_valid_entry_create(self):  
        form_data = {'full_name':"TestName",'company_name':'','email':"xyz@gmail.com",'phone_no':'','note':"Testing...",'created_when':timezone.now(),'modified_when':timezone.now()}  
        self.assertEqual(ContactUs.objects.count(), 0)
        response = self.c.post(reverse('contact_response') , form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactUs.objects.count(), 1)   
