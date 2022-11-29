from wsgiref import validate
from django import template
import mimetypes
register = template.Library()

@register.filter(name='file_type')
def getFileType(value):
    return mimetypes.guess_type(value,strict = True)[0]

@register.filter(name='get_ext')
def getFileExt(value):
    return value.split(".")[-1]