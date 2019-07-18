from django.shortcuts import render
from newone.forms import PhoneForm

# Create your views here.
def phonenumber(request):
	if request.method == 'POST':
		form = PhoneForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home:book_list')
	else:
		form = PhoneForm()
	return render(request, 'newone/phone.html', {'form': form})




