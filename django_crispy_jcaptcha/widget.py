from django.forms import Media, MediaDefiningClass, Widget, CheckboxInput
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from django_crispy_jcaptcha import models
from django.conf import settings

import binascii
import uuid
import os, hashlib
import random

class CaptchaImages(Widget):

     def __init__(self, *args, **kwargs):
         self.attrs = {'test': 'test'}


     def render(self, name, value, *args, **kwargs):
         print (settings)
         STATIC_URL = settings.STATIC_URL
         JCAPTCHA_EXPIRY_MINUTES=30
         JCAPTCHA_CLEANUP_MINUTES=1440

         if hasattr(settings,'JCAPTCHA_EXPIRY_MINUTES'):
              JCAPTCHA_EXPIRY_MINUTES=settings.JCAPTCHA_EXPIRY_MINUTES

         if hasattr(settings,'JCAPTCHA_CLEANUP_MINUTES'):
              JCAPTCHA_CLEANUP_MINUTES=settings.JCAPTCHA_CLEANUP_MINUTES
         print (JCAPTCHA_EXPIRY_MINUTES)
         print (JCAPTCHA_CLEANUP_MINUTES)

         now = datetime.now()
         expiry = now + timedelta(minutes = JCAPTCHA_EXPIRY_MINUTES)
         in_the_past = now - timedelta(minutes=JCAPTCHA_CLEANUP_MINUTES)
         cleanup_captchas = models.Captcha.objects.filter(expiry__lte=in_the_past).delete()

         id_name = 'id_'+name
         images = self.imagelist()
         random.shuffle(images)

         image_selection = images[0]
         captcha = models.Captcha.objects.create(captcha_key=hashlib.md5(os.urandom(32)).hexdigest(),captcha_image=image_selection['image'], image_key_match=image_selection['random_key'],expiry=expiry)

         image_rotation = []
         image_rotation.append(images[0])
         image_rotation.append(images[1])
         image_rotation.append(images[2])
         image_rotation.append(images[3])
         image_rotation.append(images[4])
         image_rotation.append(images[5])
         image_rotation.append(images[6])
         image_rotation.append(images[7])
         image_rotation.append(images[8])
         image_rotation.append(images[9])
         image_rotation.append(images[10])
         image_rotation.append(images[11])
         image_rotation.append(images[12])
         image_rotation.append(images[13])
         image_rotation.append(images[14])
         image_rotation.append(images[15])
         image_rotation.append(images[16])
         image_rotation.append(images[17])
         image_rotation.append(images[18])
         image_rotation.append(images[19])
         image_rotation.append(images[20])
         image_rotation.append(images[21])
         image_rotation.append(images[22])
         image_rotation.append(images[23])

        
         random.shuffle(image_rotation) 
         for im in image_rotation:
             captcha_image = models.CaptchaImage.objects.create(captcha=captcha,captcha_key=im['random_key'],captcha_image=im['image'])

         image_div = ""
         for im in image_rotation:
              image_div = image_div + "<img id='id_captcha_image_"+im['random_key']+"' onclick="+'"'+"jcaptcha.select('"+id_name+"','"+captcha.captcha_key+"','"+im['random_key']+"');"+'"'+" src='/jcaptcha/image-match/"+im['random_key']+".png' class='jcaptcha-matches' istyle='border: 1px solid #000000; padding: 3px; margin-right: 2px; cursor: pointer;'>"

         htmldata = ""
         htmldata += "<link rel='stylesheet' href='"+STATIC_URL+"/css/jcaptcha/style.css'>"
         htmldata += "<script type='text/javascript' src='"+STATIC_URL+"/js/jcaptcha/jcaptcha.js'></script>"
         htmldata += "<div id='jwidget_div_"+name+"'>"
         htmldata += "<div>Please select the matching image below: <img src='/jcaptcha/image-selection/"+captcha.captcha_key+".png' style='border: 1px solid #000000; padding: 3px; margin-right: 2px;'></div>"
         htmldata += "<div><br></div>"
         htmldata += "<div><b>Match selection</b></div>"
         htmldata += "<div style='width: 250px'>"+image_div+"</div>"
         htmldata += "<div><input type='hidden' name='"+name+"' id='"+id_name+"'>"
         htmldata += "<div><br></div>"
         htmldata += "<div><br></div>"

         return format_html(htmldata)


     def imagelist(self):
         images = [{ 'image' : '/static/images/jcaptcha/headphones-human.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/lighter.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/bomb-grenade.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/dating-rose.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/golf-hole.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/skull-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/coffee-cold.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/rat.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/rooster.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/cog.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/pin.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/office-work-wireless.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/outdoors-tree-valley.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/plane-trip-international.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/programming-flag.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/whale-body.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/send-email-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/shop-cashier-man.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/shop-cashier-woman.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/show-hat-magician-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/stamps-famous.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/tablet-touch.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/target-center-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/warehouse-storage-3.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/insurance-card.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/landmark-japan-shrine.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/laptop-smiley-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/email-action-receive.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/footwear-heels-ankle.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/hammer-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/gauge-dashboard-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/love-boat.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/maps-pin.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/medical-personnel-doctor.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/megaphone-1.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/monkey.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/mood-happy.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/mouse.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/mobile-phone-2.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},
                   { 'image' : '/static/images/jcaptcha/nautic-sports-sailing-person.png', 'random_key' : hashlib.md5(os.urandom(32)).hexdigest()},

                  ]
         return images          


def CaptchaValidation(captcha_value, forms):
    now = datetime.now()
    captcha_valid = False
    captcha_split = captcha_value.split(':')
    if len(captcha_split) == 2:
        if models.Captcha.objects.filter(captcha_key=captcha_split[0], image_key_match=captcha_split[1],expiry__gte=now).count() > 0:
            print ("captcha valid")
            captcha_valid = True 
            cap = models.Captcha.objects.filter(captcha_key=captcha_split[0], image_key_match=captcha_split[1],expiry__gte=now)
            for c in cap:
                c.expiry=now
                c.save()
            pass
        else:
            cap = models.Captcha.objects.filter(captcha_key=captcha_split[0],expiry__gte=now)
            for c in cap:
                c.expiry=now
                c.save()

            raise forms.ValidationError('Captcha selection incorrect,  please try again.')
    else:
        raise forms.ValidationError('Please select matching captcha picture.')
    
    return captcha_valid






