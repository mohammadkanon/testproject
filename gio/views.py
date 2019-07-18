from django.shortcuts import render
from gio.forms import GeoPosition

# Create your views here.
def position(request):
	if request.method == "POST":
		form = GeoPosition(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = GeoPosition()

	return render(request, 'gio/position.html', {'form': form})