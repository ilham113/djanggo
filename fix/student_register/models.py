from django.db import models

# Create your models here.

class Prodi(models.Model):
	nama_prodi = models.CharField(max_length=50)

	def __str__(self):
		return self.nama_prodi

class Mahasiswa(models.Model):
	nama = models.CharField(max_length=100)
	nim = models.CharField(max_length=12)
	tahun_masuk = models.CharField(max_length=4)
	prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)