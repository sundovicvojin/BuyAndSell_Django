# Generated by Django 5.1.2 on 2024-10-25 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodaja', '0002_komentar_ocena'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poruka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst', models.TextField()),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('posiljalac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poslate_poruke', to=settings.AUTH_USER_MODEL)),
                ('primalac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primljene_poruke', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
