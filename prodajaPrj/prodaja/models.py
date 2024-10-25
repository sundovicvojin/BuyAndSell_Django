from django.db import models
from django.contrib.auth.models import User

class Proizvod(models.Model):
    naslov = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kategorija = models.CharField(max_length=50)
    postavljen_datum = models.DateTimeField(auto_now_add=True)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.naslov

class Komentar(models.Model):
    proizvod = models.ForeignKey(Proizvod, related_name='komentari', on_delete=models.CASCADE)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    tekst = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Komentar od {self.korisnik.username} na {self.proizvod.naslov}'

class Ocena(models.Model):
    proizvod = models.ForeignKey(Proizvod, related_name='ocene', on_delete=models.CASCADE)
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    ocena = models.PositiveIntegerField()

    def __str__(self):
        return f'Ocena od {self.korisnik.username} za {self.proizvod.naslov}'


class Poruka(models.Model):
    posiljalac = models.ForeignKey(User, related_name='poslate_poruke', on_delete=models.CASCADE)
    primalac = models.ForeignKey(User, related_name='primljene_poruke', on_delete=models.CASCADE)
    tekst = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Poruka od {self.posiljalac.username} ka {self.primalac.username}'




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    broj_telefona = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.user.username} profil'
