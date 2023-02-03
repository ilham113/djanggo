from django import forms

class RegisterForm(forms.Form):
	nama			= forms.CharField(label='Nama Lengkap',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Masukkan Nama Lengkap Anda'}))
	jenis_kelamin 	= forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=[('P','Pria'),('W','Wanita')]) 
	tgl_lahir 		= forms.DateField(widget= forms.SelectDateWidget(years=range(1945,2020,1),attrs={'class':'form-control col-sm-2'}))
	alamat 			= forms.CharField(label='Alamat (Lengkap)',widget=forms.Textarea(attrs={'class':'form-control'}),max_length=100,required=False)
	email 			= forms.EmailField(label='Alamat E-Mail',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Masukkan Alamat E-Mail Anda'}))
	password 		= forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Masukkan password Anda'}),label='password')