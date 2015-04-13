from django.conf.urls import patterns, url

from note import views

urlpatterns = patterns('',
    url(r'notes\.json', views.notes, name='all_notes'),
    url(r'note/id-(?P<note_id>\d+)\.json',
                                         views.note_by_id, name='note_by_id'),
    url(r'tags\.json', views.tags, name='all_tags'),
    url(r'notes/filter/tags', views.notes_filter_by_tags,
                                                 name='notes_filter_by_tag'),
    url(r'note/save', views.save_note, name='save_note')

)