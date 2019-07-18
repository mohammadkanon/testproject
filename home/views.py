from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from blog.decorators import superuser_only, timeit, active_user_required
from home.models import TestModel


from django.core.files.storage import FileSystemStorage
from home.forms import BookForm



def upload_book(request):
	if request.method == 'POST':
		bform = BookForm(request.POST, request.FILES)
		if bform.is_valid():
			bform.save()
			# return redirect('home:book_list')
	else:
		bform = BookForm()
	return render(request, 'home/upload_book.html', {'bform': bform})


# Create your views here.
def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'home/error_404.html', data)

def error_500_view(request, *args, **argv):
    response = render_to_response('home/error_500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


# @superuser_only
# @timeit
# @active_user_required
def core(request):
	zoo = '0'
	type_of = type(zoo).__name__
	names = TestModel.objects.all()


	context = {
		'zoo': zoo,
		'names': names,
		'type_of': type_of
	}

	return render(request, 'home/file.html', context)


def upload(request):
	if request.method == 'POST':
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
	return render(request, 'home/upload.html')

def book_list(request):
	return render(request, 'home/book_list.html')
