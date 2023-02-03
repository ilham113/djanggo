from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'blog',
		'creator':'ilham',
		'nav':[
				['/gallery','gallery'],
				['/about','about'],
				['/','home']
		],

	}
	return render(request,'blog.html', context)