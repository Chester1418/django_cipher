from django.conf.urls import url
from . import views


urlpatterns = (
    url(r'^decrypt_text/', views.decrypt_text, name='decrypt_text'),
    url(r'^encrypt_text/', views.encrypt_text, name='encrypt_text'),
    url(r'^detect_rot/', views.detect_rot, name='detect'),
    url(r'^bruted/', views.bruted, name='bruted'),
    url(r'^$', views.caesar_cipher_page, name='caesar_cipher_page'),
)