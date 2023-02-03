from django import forms
from .models import Transaksi

class FormTransaksi(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = ('nama_pembeli','alamat','barang','qty')
        labels = {
            'nama_pembeli':'Nama Pembeli',
        }