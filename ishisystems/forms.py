"""ishisystemswebsite Forms"""

from django import forms
 
from  ishisystems.models import ContactUs
from  ishisystems.models import Question
import datetime

#Contact form for contact us page
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'company_name','email','phone_no','note')
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'col-md-12 form-control','placeholder':'Name','required':'true'}),
            'company_name' : forms.TextInput(attrs={'class':'col-md-12 form-control','placeholder':'Company'}),
            'email' : forms.EmailInput(attrs={'class':'col-md-12 form-control','placeholder':'Email','required':'true'}),
            'phone_no' : forms.TextInput(attrs={'class':'col-md-12 form-control','placeholder':'Phone'}),
            'note' : forms.Textarea(attrs={'class':'col-md-12 form-control','placeholder':'Note','required':'true','rows':'2'})
        } 
#Question Form for index page
class QuestionForm(forms.ModelForm):
     
    
    class Meta:
        model = Question
        fields = ('full_name', 'email','message')
        widgets = {
            'full_name': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Your Name','required':'true'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control','placeholder':'Your Email','required':'true'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control','placeholder':'Your Message','required':'true','rows':'5'}),
            
        }
     
                 