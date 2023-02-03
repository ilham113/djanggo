from django.shortcuts import render

# Create your views here.

def home(request):
	context = {
				'Heading':'Selamat Datang',
				'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis gravida leo massa, vitae bibendum libero rhoncus sed. Donec non purus tristique, blandit sapien vel, imperdiet odio. Curabitur tempor ultrices nulla vitae vestibulum. Sed tristique orci eget malesuada hendrerit. Quisque tempor nulla non iaculis malesuada. Aliquam erat volutpat. Nullam id metus efficitur urna aliquet consequat quis in nunc. Nunc elit ligula, tincidunt sit amet eros vitae, tincidunt porta risus. Maecenas purus urna, bibendum sagittis mauris nec, volutpat tempor dolor. Etiam in venenatis velit. Sed at justo elementum, condimentum risus in, lobortis nisl. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ultricies, mi ac tempor viverra, lectus metus fermentum tortor, sit amet blandit lectus tellus a sem. Mauris at metus convallis, interdum lorem quis, facilisis dui.Mauris pellentesque vitae tellus eu tincidunt. Aliquam sit amet tempor felis. Fusce ac aliquam metus. Vivamus semper, est ut scelerisque iaculis, tortor odio finibus ante, aliquet lobortis sem felis quis sapien. In bibendum felis vel lacus maximus, fringilla semper velit dictum. Morbi tempus, lacus ac pretium ullamcorper, turpis lorem cursus sapien, vitae eleifend est libero a dui. Sed non est porttitor quam congue viverra et non tortor. Nullam ultricies tincidunt tempor. In iaculis imperdiet scelerisque. Curabitur ut molestie mauris. Phasellus sed enim vel massa cursus suscipit. Sed non dictum nisi. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas lacinia, arcu nec egestas ultricies, tortor ipsum convallis elit, sed eleifend justo urna non odio. Nam semper nec lacus a elementum.'
	}
	return render(request, 'home.html',context)

def khs(request):
	context = {
		'Heading':'Kartu Hasil Study',
		'Heading2':'Semester Genap 2019/2020'
	}
	return render(request, 'khs.html',context)