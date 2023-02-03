from django.urls import path
from . import views

urlpatterns = [
	path('', views.student_form, name='tambah_mahasiswa'),
	path('<int:id>/', views.student_form, name='ubah_mahasiswa'),
	path('delete/<int:id>/', views.student_delete, name='hapus_mahasiswa'),
	path('list/', views.student_list, name='tampil_mahasiswa')
]