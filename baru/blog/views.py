from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'Title':'Blog',
		'Heading':'Blog Pertamaku',
	}
	return render(request, 'blog/index.html', context)