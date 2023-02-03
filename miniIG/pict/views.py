from django.shortcuts import render, redirect
from .models import Pict
from .forms import PictPost
from django.http import HttpResponse


def index(request):
	shelf = Pict.objects.all()
	return render(request, 'home.html', {'shelf': shelf})

def upload(request):
	upload = PictPost()
	if request.method == 'POST':
		upload = PictPost(request.POST, request.FILES)
		if upload.is_valid():
			upload.name = request.user
			upload.save()
			return redirect('home')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'Pict/upload_form.html', {'upload_form':upload})

def update_Pict(request, Pict_id):
	Pict_id = int(Pict_id)
	try:
		Pict_sel = Pict.objects.get(id = Pict_id)
	except Pict.DoesNotExist:
		return redirect('home')
	Pict_form = PictPost(request.POST or None, instance = Pict_sel)
	if Pict_form.is_valid():
		Pict_form.save()
		return redirect('home')
	return render(request, 'Pict/upload_form.html', {'upload_form':Pict_form})

def delete_Pict(request, Pict_id):
	Pict_id = int(Pict_id)
	try:
		Pict_sel = Pict.objects.get(id = Pict_id)
	except Pict.DoesNotExist:
		return redirect('home')
	Pict_sel.delete()
	return redirect('home')

