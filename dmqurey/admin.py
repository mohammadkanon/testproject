from django.contrib import admin
from dmqurey.models import Blog, Author, Entry

# Register your models here.
admin.site.register([Blog, Author, Entry])
