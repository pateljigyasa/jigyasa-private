"""Utils:Functions required by app all over"""
import re
import os
import posixpath
import stat
import urllib.parse
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch 
from django.conf import settings
from django.contrib.staticfiles import finders

register = template.Library()

"""simple tag to return active if url is current path"""
@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''

"""simple tag to return true or false if parameter url is current path"""
@register.assignment_tag(takes_context=True)
def bool_match_url_with_current_path(context,pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
        
    path = context['request'].path
     
    if re.search(pattern, path): 
        return True
    
    return False

"""simple tag to return version based on time of last modification of file from stat"""
@register.simple_tag
def version(path): 
    normalized_path = posixpath.normpath(urllib.parse.unquote(path)).lstrip('/')
    absolute_path = finders.find(normalized_path)
    if not absolute_path and getattr(settings, 'STATIC_ROOT', None):
        absolute_path = os.path.join(settings.STATIC_ROOT, path)
    if absolute_path:
        return '%s%s?v=%s' % (settings.STATIC_URL, path, os.stat(absolute_path)[stat.ST_MTIME])
    return path

 