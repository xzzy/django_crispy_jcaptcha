from django.contrib.admin import register, ModelAdmin
from django.contrib.gis import admin
from django_crispy_jcaptcha import models

@register(models.Captcha)
class CaptchaAdmin(ModelAdmin):
    list_display = ('captcha_key', 'captcha_image', )
    search_fields = ('captcha_key',)

@register(models.CaptchaImage)
class CaptchaAdmin(ModelAdmin):
    list_display = ('captcha', 'captcha_key', 'captcha_image', )
    search_fields = ('captcha_key',)


