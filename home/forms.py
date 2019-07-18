from django import forms
from PIL import Image

from image_cropping import ImageCropWidget
from home.models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'pdf', 'cover']

	def save(self, commit=False):
		this_obj = super().save(commit=True)

		image = Image.open(self.cleaned_data['cover']) # Open image using self
		width  = image.size[0]
		height = image.size[1]

		aspect = width / float(height)

		ideal_width = 200
		ideal_height = 200

		ideal_aspect = ideal_width / float(ideal_height)

		if aspect > ideal_aspect:
			# Then crop the left and right edges:
		    new_width = int(ideal_aspect * height)
		    offset = (width - new_width) / 2
		    resize = (offset, 0, width - offset, height)

		else:
			# ... crop the top and bottom:
		    new_height = int(width / ideal_aspect)
		    offset = (height - new_height) / 2
		    resize = (0, offset, width, height - offset)

		thumb = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)
		thumb.save(this_obj.cover.path)



		# area = (400, 400, 800, 800)
		# img = img.crop(area)
		# img.save(this_obj.cover.path)  # saving image at the same path

		# return img

