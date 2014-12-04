from django.contrib import admin

from note.models.note import Note
from note.models.tag import Tag

# Register your models here.
admin.site.register(Note)
admin.site.register(Tag)