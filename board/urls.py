from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('example/',views.example,name='example'),
    path('card/',views.card,name='card'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]