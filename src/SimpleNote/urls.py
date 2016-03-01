from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('webapp.urls')),
    url(r'^ap/', include('note.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', django.contrib.auth.views.login)
]
