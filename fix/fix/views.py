from django.shortcuts import render
 
from .forms import RegisterForm 

# Create your views here.

def index(request):
	register_form = RegisterForm()
	context = {
		'Title':'HOME',
		'Heading':'Form Register',
		'Register_Form':register_form
	}
	if request.method == 'POST':
		context['nama'] 			= request.POST['nama']
		context['jenis_kelamin'] 	= request.POST['jenis_kelamin']
		#context['tgl_lahir'] 		= request.POST['tgl_lahir']
		context['alamat'] 			= request.POST['alamat']
		context['email'] 			= request.POST['email']
		context['password'] 		= request.POST['password']

	return render(request, 'index.html', context)