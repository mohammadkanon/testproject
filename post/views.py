from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from post.models import Author

from post.forms import ContactForm

class ContactView(FormView):
	template_name = 'post/contact.hatml'
	form_class = ContactForm
	success_url = '/thanks/'

	def form_valid(self, form):
		return super().formvalid(form)



class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
