"""Context Processor for constants for website"""
from django.conf import settings # import the settings file

#Linkedin url
def app_linkedin_url(context):

    return {'APP_LINKEDIN_URL': settings.APP_LINKEDIN_URL}
#Twittwer Url
def app_twitter_url(context):
    
    return {'APP_TWITTER_URL' : settings.APP_TWITTER_URL}
#APP BLOG_URl
def app_blog_url(context):
    
    return {'APP_BLOG_URL' : settings.APP_BLOG_URL}
#REQUEST email address
def app_request_email_address(context): 
    return {'APP_REQUEST_EMAIL_ADDRESS' : settings.APP_REQUEST_EMAIL_ADDRESS}
#Careers Email address
def app_careers_email_address(context):
    
    return {'APP_CAREERS_EMAIL_ADDRESS' : settings.APP_CAREERS_EMAIL_ADDRESS}

#Directions path website address
def app_directions_path_website(context):
    
    return {'APP_DIRECTIONS_PATH_WEBSITE' : settings.APP_DIRECTIONS_PATH_WEBSITE}

#CONTACT US email address
def app_contactus_email_address(context):
    
    return {'APP_CONTACTUS_EMAIL_ADDRESS' : settings.APP_CONTACTUS_EMAIL_ADDRESS}

def app_cloud_native_download_link(context):
    
    return {'APP_CLOUD_NATIVE_WHITEPAPER_DOWNLOAD_LINK' : settings.APP_CLOUD_NATIVE_WHITEPAPER_DOWNLOAD_LINK}

def app_cloud_native_brochure_download_link(context):

    return {'APP_CLOUD_NATIVE_BROCHURE_DOWNLOAD_LINK' : settings.APP_CLOUD_NATIVE_BROCHURE_DOWNLOAD_LINK}

def app_carousel_learn_more_link(context):

    return {'APP_CAROUSEL_LEARN_MORE_LINK' : settings.APP_CAROUSEL_LEARN_MORE_LINK}