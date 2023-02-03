from django.shortcuts import render

def index(request):
	context = {
		'judul':'home',
		'creator':'ilham',
		'nav':[
				['/gallery','gallery'],
				['/about','about'],
				['/blog','blog']
		],

	}
	return render(request,'index.html', context)