# Generated by Django 5.1.2 on 2024-10-25 00:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodaja', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst', models.TextField()),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('korisnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proizvod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentari', to='prodaja.proizvod')),
            ],
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocena', models.PositiveIntegerField()),
                ('korisnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proizvod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ocene', to='prodaja.proizvod')),
            ],
        ),
    ]
