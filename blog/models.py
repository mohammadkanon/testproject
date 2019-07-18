from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	content = models.TextField(null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	creation_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Entry'
		verbose_name_plural = 'Entries'

	def __str__(self):
		return self.title
