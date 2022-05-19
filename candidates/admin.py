from django.contrib import admin
from .models import Candidate, Tag, Value

admin.site.register(Candidate)
admin.site.register(Tag)
admin.site.register(Value)
