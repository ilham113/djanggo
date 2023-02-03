from django.shortcuts import render, redirect
from .forms import FormTransaksi
from .models import Transaksi,Barang

# Create your views here.
def form(request,id=0):
    form = FormTransaksi()
    if request.method == 'POST':
        if id == 0:
            form = FormTransaksi(request.POST)
        else:
            transaksi = Transaksi.objects.get(pk=id)
            form = FormTransaksi(request.POST,instance=transaksi)
        form.save()
        return redirect('/')
    else:
        if id == 0:
            form = FormTransaksi()
        else:
            transaksi = Transaksi.objects.get(pk=id)
            form = FormTransaksi(instance=transaksi)
        return render(request, "transaksi/form.html",{'form':form})

def delete(request,id):
    transaksi = Transaksi.objects.get(pk=id)
    transaksi.delete()
    return redirect('/')