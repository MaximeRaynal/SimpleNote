from django.conf.urls import patterns, url

from note import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'notes\.json', views.)
)