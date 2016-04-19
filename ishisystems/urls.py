""" URL configuraton for ishisystem website""" 
from django.conf.urls import url
from . import views 
from django.conf.global_settings import STATICFILES_DIRS
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^capabilities/$', views.capabilities, name='capabilities'), 
    url(r'^high-performance/$', views.high_performance, name='high_performance'), 
    url(r'^big-data/$', views.big_data, name='big_data'), 
    url(r'^cloudnative/$', views.cloud_native, name='cloud_native'), 
    url(r'^case-study-big-data/$', views.case_study_big_data, name='case_study_big_data'), 
    url(r'^realtime-stream-processing/$', views.real_time, name='real_time.html'), 
    url(r'^case-study-high-performance-computing/$', views.case_study_high_performance_computing, name='case_study_high_performance_computing.html'), 
    url(r'^datacenter/$', views.datacenter, name='datacenter.html'), 
    url(r'^case-study-data-center-scaling/$', views.case_study_data_center_scaling, name='case_study_data_center_scaling.html'), 
    url(r'^case-study-real-time/$', views.case_study_real_time,   name ='case_study_real_time.html'), 
    url(r'^services/$', views.services, name='services'), 
    url(r'^managed-solutions/$', views.managed_solutions, name='managed_solutions'),
    url(r'^services-framework/$', views.services_framework, name='services_framework'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^about/$', views.about, name='about'),
    url(r'^careers/$', views.careers, name='careers'),
    url(r'^benefits-us/$', views.benefits_us, name='benefits_us.html'),
    url(r'^benefits-switzerland/$', views.benefits_switzerland, name='benefits_switzerland.html'),
    url(r'^benefits-india/$', views.benefits_india, name='benefits_india.html'),
    url(r'^jobs/(?P<loc>[a-zA-Z]+)/(?P<pos>[0-9]+)$', views.jobs, name='jobs.html'),
    url(r'^contactus/$', views.contactus, name='contactus.html'),
    url(r'^directions/$', views.directions, name='directions.html'),
    url(r'^contact-response/$', views.contact_response,name='contact_response'),
    url(r'^question-response/$', views.question_response,name='question_response'),
    url(r'^response-thanks/$', views.response_thanks)
 
    
   ] 
 

 