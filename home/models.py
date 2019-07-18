from django.db import models
from home.validators import validate_file_size

from django.core.exceptions import ValidationError

from PIL import Image
from image_cropping import ImageCropField, ImageRatioField



# Create your models here.

class TestModel(models.Model):
	name = models.TextField(null=True)




def validate_image(image):
    file_size = image.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='books/pdfs/', validators=[validate_file_size], null=True, blank=True)
	cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

	class Meta:
		verbose_name = 'book'
		verbose_name_plural = 'books'

	def __str__(self):
		return self.title