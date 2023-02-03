from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
	class Meta:
		model = Mahasiswa
		fields = ('nama','nim','tahun_masuk','prodi')
		labels = {
			'nama':'Nama Lengkap',
			'nim':'NIM',
			'tahun_masuk':'Tahun Masuk',
			'prodi':'Program Studi'
		}