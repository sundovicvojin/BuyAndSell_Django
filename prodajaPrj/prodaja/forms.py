from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Komentar, Ocena
from .models import Proizvod
from .models import Poruka
from .models import Profile

class PretragaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Pretraga')

class FilterForm(forms.Form):
    min_cena = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Minimalna cena')
    max_cena = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Maksimalna cena')
    kategorija = forms.CharField(max_length=50, required=False, label='Kategorija')

class KorisnickaRegistracijaForma(UserCreationForm):
    email = forms.EmailField(required=True)
    broj_telefona = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'broj_telefona', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(user=user)
            profile.broj_telefona = self.cleaned_data['broj_telefona']
            profile.save()
        return user



class ProizvodForma(forms.ModelForm):
    class Meta:
        model = Proizvod
        fields = ['naslov', 'opis', 'cena', 'kategorija']



class KomentarForma(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['tekst']

class OcenaForma(forms.ModelForm):
    class Meta:
        model = Ocena
        fields = ['ocena']



class PorukaForma(forms.ModelForm):
    class Meta:
        model = Poruka
        fields = ['primalac', 'tekst']



class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email']

class PasswordUpdateForm(forms.ModelForm):
    password1 = forms.CharField(label='Nova šifra', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potvrdi šifru', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Šifre se ne poklapaju.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
