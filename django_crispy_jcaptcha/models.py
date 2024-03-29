from __future__ import unicode_literals
from datetime import timedelta
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
#from django.core.urlresolvers import reverse
#from django.utils.encoding import python_2_unicode_compatible
#from model_utils import Choices
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

#@python_2_unicode_compatible
class Captcha(models.Model):

    captcha_key = models.CharField(max_length=256)
    image_key_match = models.CharField(max_length=256)
    captcha_image = models.CharField(max_length=256)
    expiry = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return self.captcha_key


#@python_2_unicode_compatible
class CaptchaImage(models.Model):

    captcha = models.ForeignKey(Captcha, blank=True, null=True, on_delete=models.CASCADE)
    captcha_key = models.CharField(max_length=256)
    captcha_image = models.CharField(max_length=256)


    def __str__(self):
        return self.captcha_key


