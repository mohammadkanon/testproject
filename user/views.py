from django.shortcuts import render

# Create your views here.

def log_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form
	}
	next = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = nest_ or next_post or None
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_sate_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect('/')

		else:
		# return an 'invalid login' error message
		print('Error')
	return render(request, 'user/login.html', context)


User = get_user_model()

def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form': form
	}
	if form.is_valid:
		form.save:
	return render(request, 'user/register.html', context)

