from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'gallery',
		'creator':'ilham',
		'nav':[
				['/','home'],
				['/gallery/pantai','pantai'],
				['/gallery/pegunungan','pegunungan']
		]
	}
	return render(request,'gallery.html', context)