from django.contrib import admin

from note.models import Note
from note.models import Tag

# Register your models here.
admin.site.register(Note)
admin.site.register(Tag)