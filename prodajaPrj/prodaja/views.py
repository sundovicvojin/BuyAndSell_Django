from .forms import PretragaForm, FilterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import KorisnickaRegistracijaForma
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proizvod
from django.contrib.auth import views as auth_views

class PrilagodjeniLoginView(auth_views.LoginView):
    template_name = 'prodavnica/login.html'

def home(request):
    pretraga_form = PretragaForm()
    filter_form = FilterForm()
    query = request.GET.get('query')
    proizvodi = Proizvod.objects.all()
    if query:
        proizvodi = proizvodi.filter(naslov__icontains=query)
    min_cena = request.GET.get('min_cena')
    max_cena = request.GET.get('max_cena')
    kategorija = request.GET.get('kategorija')
    if min_cena:
        proizvodi = proizvodi.filter(cena__gte=min_cena)
    if max_cena:
        proizvodi = proizvodi.filter(cena__lte=max_cena)
    if kategorija:
        proizvodi = proizvodi.filter(kategorija__icontains=kategorija)
    context = {
        'proizvodi': proizvodi,
        'pretraga_form': pretraga_form,
        'filter_form': filter_form
    }
    return render(request, 'prodavnica/home.html', context)

def registracija(request):
    if request.method == 'POST':
        form = KorisnickaRegistracijaForma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = KorisnickaRegistracijaForma()
    return render(request, 'prodavnica/registracija.html', {'form': form})



@login_required
def dodaj_proizvod(request):
    if request.method == 'POST':
        form = ProizvodForma(request.POST)
        if form.is_valid():
            proizvod = form.save(commit=False)
            proizvod.korisnik = request.user
            proizvod.save()
            return redirect('home')
    else:
        form = ProizvodForma()
    return render(request, 'prodavnica/dodaj_proizvod.html', {'form': form})




@login_required
def dodaj_komentar(request, proizvod_id):
    proizvod = get_object_or_404(Proizvod, id=proizvod_id)
    if request.method == 'POST':
        form = KomentarForma(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.proizvod = proizvod
            komentar.korisnik = request.user
            komentar.save()
            return redirect('home')
    else:
        form = KomentarForma()
    return render(request, 'prodavnica/dodaj_komentar.html', {'form': form})

@login_required
def dodaj_ocenu(request, proizvod_id):
    proizvod = get_object_or_404(Proizvod, id=proizvod_id)
    if request.method == 'POST':
        form = OcenaForma(request.POST)
        if form.is_valid():
            ocena = form.save(commit=False)
            ocena.proizvod = proizvod
            ocena.korisnik = request.user
            ocena.save()
            return redirect('home')
    else:
        form = OcenaForma()
    return render(request, 'prodavnica/dodaj_ocenu.html', {'form': form})

@login_required
def posalji_poruku(request):
    if request.method == 'POST':
        form = PorukaForma(request.POST)
        if form.is_valid():
            poruka = form.save(commit=False)
            poruka.posiljalac = request.user
            poruka.save()
            return redirect('home')
    else:
        form = PorukaForma()
    return render(request, 'prodavnica/posalji_poruku.html', {'form': form})

@login_required
def profile_settings(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user)
        pass_form = PasswordUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and pass_form.is_valid():
            p_form.save()
            pass_form.save()
            return redirect('profile_settings')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        pass_form = PasswordUpdateForm(instance=request.user)
    return render(request, 'prodavnica/profile_settings.html', {
        'p_form': p_form,
        'pass_form': pass_form
    })

@login_required
def primljene_poruke(request):
    poruke = Poruka.objects.filter(primalac=request.user)
    return render(request, 'prodavnica/primljene_poruke.html', {'poruke': poruke})