"""Views for ishisystems website"""

from django.shortcuts import render
from ishisystems.models import Client
from ishisystems.models import People
from ishisystems.models import Job
from ishisystems.models import ContactUs
from ishisystems.forms import ContactForm, QuestionForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.forms.forms import Form 
from django.utils import timezone
import json
from ishisystemswebsite.settings import APP_CONTACTUS_EMAIL_ADDRESS

# Create your views here.
#Index view 
def index(request):
    form=QuestionForm()
    return render(request, 'index.html', {'form':form})
#Capabilities from header
def capabilities(request):
    return render(request, 'capabilities.html', {})
def high_performance(request):
    return render(request, 'high_performance.html', {})
def big_data(request):
    return render(request, 'big_data.html', {})
def cloud_native(request):
    return render(request, 'cloud_native.html', {})
def case_study_big_data(request):
    return render(request, 'case_study_big_data.html', {})
def real_time(request):
    return render(request, 'real_time.html', {})
def case_study_high_performance_computing(request):
    return render(request, 'case_study_high_performance_computing.html', {})
def datacenter(request):
    return render(request, 'datacenter.html', {})
def case_study_data_center_scaling(request):
    return render(request, 'case_study_data_center_scaling.html', {})
def case_study_real_time(request):
    return render(request, 'case_study_real_time.html', {})
#services and solutions from header
def services(request):
    return render(request, 'services.html', {})
def managed_solutions(request):
    return render(request, 'managed_solutions.html', {})
def services_framework(request):
    return render(request, 'services_framework.html', {})
def clients(request): 
    clients_list = Client.objects.order_by('id')
    context_dict = {'clients': clients_list} 
    return render(request, 'clients.html', context_dict)
#About from header
def about(request):
    people_js = [] 
    peoples_list = People.objects.all()
    for people in peoples_list:
        people_js.append([people.first_name,people.img_path])
     
    context_dict = {'peoples': json.dumps(people_js)} 
    
    return render(request, 'about.html', context_dict)

def careers(request): 
    #===========================================================================
    # jobs_us = []
    # jobs_ch = []
    # jobs_in = []
    # jobs_us_list = Job.objects.filter(country_name="USA")
    # jobs_ch_list = Job.objects.filter(country_name="Switzerland")
    # jobs_in_list = Job.objects.filter(country_name="India")
    # for job in jobs_us_list:
    #     jobs_us.append([job.position,job.skills_set,job.type,job.city,job.job_detail_page,job.compensation])
    # for job in jobs_ch_list:
    #     jobs_ch.append([job.position,job.skills_set,job.type,job.city,job.job_detail_page,job.compensation])
    # for job in jobs_in_list:
    #     jobs_in.append([job.position,job.skills_set,job.type,job.city,job.job_detail_page,job.compensation])
    # context_dict = {'jobs_us': json.dumps(jobs_us),'jobs_ch': json.dumps(jobs_ch),'jobs_in': json.dumps(jobs_in)} */
    # return render(request, 'careers.html',context_dict)
    #===========================================================================
    jobs_list = Job.objects.all()
    dict_ = {};
    jobs = [];
    for job in jobs_list:
        jobs.append([job.position,job.skills_set,job.type,job.city,job.job_detail_page,job.compensation,job.country_name]) 
    context_dict = {'jobs_data': json.dumps(jobs)} 
    return render(request, 'careers.html',context_dict)
def benefits_us(request):  
    return render(request, 'benefits_us.html',{})
def benefits_switzerland(request):  
    return render(request, 'benefits_switzerland.html',{})
def benefits_india(request):  
    return render(request, 'benefits_india.html',{})
def jobs(request,loc='USA',pos=1):  
    jobs_loc = []
    job_loc_list = Job.objects.filter(country_name=loc)
    for job in job_loc_list:
        jobs_loc.append([job.position,job.skills_set,job.type,job.city,job.job_detail_page])
    context_dict = {"loc":loc,"pos":pos,"jobs_loc":json.dumps(jobs_loc)}
    return render(request, 'jobs.html',context_dict)
def contactus(request):
    form = ContactForm() 
    return render(request, 'contactus.html', {'form':form})
def directions(request):
    return render(request, 'directions.html', {})
#Response method for contact which will send mail.
def contact_response(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            contact = form.save(commit=False) 
            contact.created_when = timezone.now()
            contact.modified_when = timezone.now()
            contact.save() 
            try:
                if(cd['full_name']): 
                    emailmsg = "Name: " + cd['full_name'] +"\n"
                if(cd['company_name']):
                    emailmsg += "Company: " + cd['company_name'] + "\n"
                if(cd['phone_no']):
                    emailmsg += "Phone: " + cd['phone_no'] + "\n"
                if(cd['note']):
                    emailmsg += "Note: " + cd['note'] + "\n"
                send_mail(
                    cd['full_name'],
                    emailmsg,
                    cd['email'],
                    [APP_CONTACTUS_EMAIL_ADDRESS],
                )
                
            except:
                return HttpResponseRedirect('/response-thanks/')
        
        
        #=======================================================================
        #Only for testing purpose for test cases
        #else:
        #     return render(request, "contactus.html", {'form': form}) 
        #=======================================================================
        
    return HttpResponseRedirect('/response-thanks/') 

#Thankyou template for contact and question  
def response_thanks(request):
    return render(request, 'response_thanks.html', {})
#Response method for question which will send mail.
def question_response(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            question = form.save(commit=False) 
            question.created_when = timezone.now()
            question.modified_when = timezone.now()
            question.save()  
            try: 
                send_mail(
                    cd['full_name'],
                    cd['message'],
                    cd['email'],
                    [APP_CONTACTUS_EMAIL_ADDRESS],
                ) 
            except:
                return HttpResponseRedirect('/response-thanks/')
        #Only for testing purpose for test cases
        #else: 
            #return render(request, "index.html", {'form': form})
    return HttpResponseRedirect('/response-thanks/')  
 
    
     
 



 
