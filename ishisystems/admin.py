from django.contrib import admin

# Register your models here.
 

from .models import Question,ContactUs,People,Job,Client


class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('name','img_path','description',),
        }),
        ('Date Information', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('created_when', 'modified_when',),
        }),
        
    )
    list_display = ('name', 'img_path','description','created_when','modified_when')
    list_filter = ['name','id','created_when','modified_when']
    search_fields = ['name','id',]
    change_list_template = "admin/change_list_filter_sidebar.html"
    
class JobAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('country_name','city','position','type','skills_set','compensation','job_detail_page',),
        }),
        ('Date Information', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('created_when', 'modified_when',),
        }),
        
    )
    list_display = ('country_name','city','position','type','skills_set','compensation','job_detail_page','created_when','modified_when')
    list_filter = ['country_name','city','position','type','compensation','created_when','modified_when']
    search_fields = ['country_name','city','position','type','compensation']
    change_list_template = "admin/change_list_filter_sidebar.html"
    
     
class PeopleAdmin(admin.ModelAdmin):
    fieldsets = ( 
        ('Full Name', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('first_name', 'last_name',),
        }),
        ('',
          {
            'fields': ('img_path','position',),
        }),
        ('Date Information', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('created_when', 'modified_when',),
        }),
        
    )
    list_display = ('first_name','last_name','img_path','position','created_when','modified_when')
    list_filter = ['first_name','last_name','img_path','position','created_when','modified_when']
    search_fields = ['first_name','last_name','img_path','position']
    change_list_template = "admin/change_list_filter_sidebar.html"

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (  
        ('',
          {
            'fields': ('full_name','email','message'),
        }),
        ('Date Information', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('created_when', 'modified_when',),
        }),
        
    )
    list_display = ('full_name','email','message','created_when','modified_when')
    list_filter = ['full_name','email','message','created_when','modified_when']
    search_fields = ['full_name','email','id']
    change_list_template = "admin/change_list_filter_sidebar.html"

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (  
        ('',
          {
            'fields': ('full_name','company_name','email','phone_no','note'),
        }),
        ('Date Information', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('created_when', 'modified_when',),
        }),
        
    )
    list_display = ('full_name','company_name','email','phone_no','note','created_when','modified_when')
    list_filter = ['full_name','company_name','email','phone_no','note','created_when','modified_when']
    search_fields = ['full_name','company_name','email','phone_no']
    change_list_template = "admin/change_list_filter_sidebar.html"

 
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(ContactUs,ContactAdmin)
admin.site.register(People,PeopleAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Client,ClientAdmin)
 
 