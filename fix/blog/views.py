from django.shortcuts import render
 
from .models import Post

# Create your views here.

def index(request):
	postingan = Post.objects.all()
	context = {
		'Title':'Blog',
		'Heading':'Blog Pertamaku',
		'Postingan':postingan,
	}
	return render(request, 'blog/index.html', context)