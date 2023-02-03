from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='tambah'),
    path('<int:id>/', views.form, name='ubah'),
    path('delete/<int:id>/', views.delete, name='hapus'),
]