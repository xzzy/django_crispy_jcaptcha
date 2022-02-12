from __future__ import unicode_literals
from datetime import datetime, date, timedelta
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import re
from datetime import datetime, timedelta
import math
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import get_template
import json
import os.path
import mimetypes
from django_crispy_jcaptcha import models


def getImagePrimary(request,hashkey,extension):
    pass
    PLUGIN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'django_crispy_jcaptcha')
    print (models.Captcha.objects.filter(captcha_key=hashkey))
    captcha_image = models.Captcha.objects.filter(captcha_key=hashkey)
    file_path = PLUGIN_DIR + captcha_image[0].captcha_image
    print (file_path)
    if os.path.isfile(file_path) is True:
         the_file = open(file_path, 'rb')
         the_data = the_file.read()
         the_file.close()
         return HttpResponse(the_data, content_type=mimetypes.types_map['.'+str(extension)])


def getImageHash(request,hashkey,extension):
    PLUGIN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'django_crispy_jcaptcha')
    captcha_image = models.CaptchaImage.objects.filter(captcha_key=hashkey)
    file_path = PLUGIN_DIR + captcha_image[0].captcha_image
    print (file_path)
    if os.path.isfile(file_path) is True:
         the_file = open(file_path, 'rb')
         the_data = the_file.read()
         the_file.close()
         return HttpResponse(the_data, content_type=mimetypes.types_map['.'+str(extension)])
    #./images/jcaptcha/coffee-cold.png


#  allow_access = False
  #if request.user.is_superuser:
#  file_record = Record.objects.get(id=file_id)
#  app_id = file_record.file_group_ref_id
#  app_group = file_record.file_group
#  if allow_access == True:
#      file_record = Record.objects.get(id=file_id)
#      file_name_path = file_record.upload.path
#      if os.path.isfile(file_name_path) is True:
#              the_file = open(file_name_path, 'rb')
#              the_data = the_file.read()
#              the_file.close()
#              if extension == 'msg':
#                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")
#              if extension == 'eml':
#                  return HttpResponse(the_data, content_type="application/vnd.ms-outlook")
#
#
#              return HttpResponse(the_data, content_type=mimetypes.types_map['.'+str(extension)])
#  else:
#              return
#
