from django import forms
from newone.models import PhoneModel
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PhoneForm(forms.ModelForm):

	phone = PhoneNumberField(max_length=200, label="Phone Number", widget=PhoneNumberPrefixWidget(), required=True)    # CharField would also work

	class Meta:
		model = PhoneModel
		fields = ['name', 'phone']