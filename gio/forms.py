from django import forms

from gio.models import PointOfInterest

class GeoPosition(forms.ModelForm):
	class Meta:
		model = PointOfInterest
		fields =['name', 'position']

