from django.contrib import admin
from .models import Document, BaseUser


admin.site.register(Document)
admin.site.register(BaseUser)
# Register your models here.
