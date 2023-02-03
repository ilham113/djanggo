from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'about',
		'creator':'ilham',
		'nav':[
				['/gallery','gallery'],
				['/blog','blog'],
				['/','home']
		],

	}
	return render(request,'about.html', context)