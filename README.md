# django_crispy_jcaptcha
This plugin allow you to integrate captcha into crispy forms as a widget.   This is django crispy forms plugin.

# Requirements

- Python (3.x.x)
- PostgreSQL (>=9.3)
- Django (>=1.11.x)


# settings.py

These are defautls but can also be added to settings.py if you wish to change the default settings.

    JCAPTCHA_EXPIRY_MINUTES=30
    JCAPTCHA_CLEANUP_MINUTES=1440

INSTALLED_APPS needs to append 'django_crispy_jcaptcha'

# forms.py

Instructions on how to ammend to your crispy form python file.

    from django_crispy_jcaptcha.widget import CaptchaImages, CaptchaValidation

    captcha = CharField(required=False,widget=CaptchaImages(attrs={}))

Inside the meta form class you will need append this def for validation.

    def clean_captcha(self):
        CaptchaValidation(self.cleaned_data['captcha'], forms)
        return self.cleaned_data['captcha']


# urls.py
Add Urls, path or url depending on django version  

url('^', include(jcaptchaurls))

or

path('', include(jcaptchaurls))

