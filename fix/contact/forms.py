from django import forms

class ContactForm(forms.Form):
	nama		= forms.CharField(label='Nama Lengkap',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Masukkan Nama Lengkap Anda'}))
	email 		= forms.EmailField(label='Alamat E-Mail',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Masukkan Alamat E-Mail Anda'}))
	pesan		= forms.CharField(label='Kesan&pesan ',widget=forms.Textarea(attrs={'class':'form-control'}),max_length=100,required=False)