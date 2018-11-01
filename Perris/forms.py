from django import forms
from .models import Adoptar, Adoptado
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

class AdoptarForm(forms.ModelForm):

    class Meta:
        model = Adoptar
        fields = ('nombreCompleto', 'run', 'correo', 'telefono')

    def clean_nombreCompleto(self):
        nombreCompleto = self.cleaned_data['nombreCompleto']
        if len(nombreCompleto.split(' ')) < 4 :
            raise ValidationError("Ingresa tu nombre completo")
        return nombreCompleto

    def clean_run(self):
        run = self.cleaned_data['run']
        if not "-" in run:
            raise ValidationError("Digite Run con guion")
        elif len(run) <= 8:
            raise ValidationError("Ingrese Run con 9 caracteres minimo")
        return run

    def clean_correo(self):
        correo = self.cleaned_data['correo']

        correo_base, proveedor = correo.split("@")
        dominio, extension = proveedor.split(".")
        if not dominio == "gmail":
            raise ValidationError("Por favor usa Gmail")
        elif not extension == "com":
            raise ValidationError("agrega .com a gmail")
        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('Respete los campos')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa 9 digitos o más")
        return telefono

class AdoptadoForm(forms.ModelForm):

    class Meta:
        model = Adoptado
        fields = ('id', 'estado')