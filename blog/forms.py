from django import forms
from blog.models import Entry

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ('title', 'slug', 'content')

	def save(self, this_user, commit=False):
		this_obj = super().save(commit=False)
		this_obj.author = this_user
		this_obj.save()

		return this_obj


