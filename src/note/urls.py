from django.conf.urls import patterns, url

from note import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'notes\.json', views.notes, name='all_notes'),
    url(r'tags\.json', views.tags, name='all_tags'),
    url(r'notes/filter/tags', views.tags, name='notes_filter_by_tag')

)