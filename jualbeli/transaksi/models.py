from django.db import models

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga = models.PositiveIntegerField()

    def __str__(self):
        return self.nama_barang

class Transaksi (models.Model):
    nama_pembeli = models.CharField(max_length=100)
    alamat = models.TextField(null=True)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    total_bayar = models.PositiveIntegerField(null=True)

    def get_total_bayar(self):
    	total = self.barang.harga * self.qty
    	return total

    def save(self, *args, **kwargs):
    	self.total_bayar = self.get_total_bayar()
    	super(Transaksi, self).save(*args, **kwargs)