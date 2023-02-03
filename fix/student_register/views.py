from django.shortcuts import render, redirect
from .forms import MahasiswaForm
from .models import Mahasiswa

# Create your views here.

def student_list(request):
	context= {
		'siswa' : Mahasiswa.objects.all()
		}
	return render(request, 'student_register/student_list.html',context)

def student_form(request, id=0):
		#context = {
	#	'form':form
	#}
	if request.method == "POST":
		if id == 0 :
			form = MahasiswaForm(request.POST)
		else:
			mhs = Mahasiswa.objects.get(pk=id)
			form = MahasiswaForm(request.POST,instance=mhs)
		form.save()
		return redirect('/student/list')


	#if request.method == 'POST':
	#	form = MahasiswaForm(request.POST)
	#	form.save()
	#	return redirect('/student/list')
	else:
		if id == 0 :
			form = MahasiswaForm()
		else:
			mhs = Mahasiswa.objects.get(pk=id)
			form = MahasiswaForm(instance=mhs)
		return render(request, 'student_register/student_form.html',{'form':form})

def student_delete(request,id):
	mhs = Mahasiswa.objects.get(pk=id)
	mhs.delete()
	return redirect('/student/list')	

		
