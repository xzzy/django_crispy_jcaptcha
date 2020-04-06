from django.conf.urls import url
from django_crispy_jcaptcha import views

urlpatterns = [
    url(r'^jcaptcha/image-selection/(?P<hashkey>\w+).(?P<extension>\w\w\w)$', views.getImagePrimary, name='jcaptcha-image-primary'),
    url(r'^jcaptcha/image-match/(?P<hashkey>\w+).(?P<extension>\w\w\w)$', views.getImageHash, name='jcaptcha-image-match'),
]
