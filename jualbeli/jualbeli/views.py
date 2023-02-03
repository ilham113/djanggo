from django.shortcuts import render
from transaksi.models import *

# Create your views here.
def index(request):
    context = {
        'daftar_transaksi':Transaksi.objects.all(),
    }
    return render(request, "daftar_transaksi.html",context)