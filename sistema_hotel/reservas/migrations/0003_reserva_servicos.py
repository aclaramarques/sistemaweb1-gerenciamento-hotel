# Generated by Django 4.2.11 on 2025-07-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos_adicionais', '0001_initial'),
        ('reservas', '0002_alter_reserva_valor_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='servicos',
            field=models.ManyToManyField(blank=True, to='servicos_adicionais.servicos_adicionais'),
        ),
    ]
