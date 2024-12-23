from django.contrib import admin

# Register your models here.
from catalog.models import Author, mail

admin.site.register(mail)
admin.site.register(Author)