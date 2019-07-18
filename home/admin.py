from django.contrib import admin           
from image_cropping import ImageCroppingMixin 
from home.models import TestModel, Book

# Register your models here.
admin.site.register(TestModel)

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):          
	pass          

admin.site.register(Book, MyModelAdmin)