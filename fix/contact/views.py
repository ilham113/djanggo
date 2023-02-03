from django.shortcuts import render
from .forms import ContactForm 

# Create your views here.

def index(request):
	register_form = ContactForm()
	context = {
		'Title':'HOME',
		'Heading':'Form Register',
		'Register_Form':register_form
	}
	if request.method == 'POST':
		context['nama'] = request.POST['nama']
		context['email'] = request.POST['email']
		context['pesan'] = request.POST['pesan']

	return render(request, 'contact/index.html', context)