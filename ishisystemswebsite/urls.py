"""ishisystemswebsite URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

    
urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ishisystems.urls')), 
     
]

