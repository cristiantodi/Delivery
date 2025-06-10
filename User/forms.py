from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Cargo

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'cargo')  # <-- incluye 'tipo'

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'cargo')

class RegistroClienteForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            cargo_cliente, _ = Cargo.objects.get_or_create(nombre__iexact='Cliente')
            user.cargo.set([cargo_cliente])  # asignación correcta
        return user
        