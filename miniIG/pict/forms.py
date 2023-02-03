from django import forms
from .models import Pict

#DataFlair
class PictPost(forms.ModelForm):

	class Meta:
		model = Pict
		fields = ('name','picture','describe')
		