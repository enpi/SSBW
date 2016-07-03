from django import forms

class RestauranteForm(forms.Form):
	nombre = forms.CharField(label='Nombre', max_length=30)
	descripcion = forms.CharField(label='Descripcion', max_length=300)
	file = forms.FileField(label='Foto')