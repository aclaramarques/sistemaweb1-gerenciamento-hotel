# Generated by Django 4.2.11 on 2025-07-15 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quartos', '0003_remove_quarto_id_alter_quarto_numero'),
        ('clientes', '0002_remove_hospede_id_hospede_cpf_alter_hospede_ativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtEntrada', models.DateField()),
                ('dtSaida', models.DateField()),
                ('quantPessoas', models.PositiveIntegerField()),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hospede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.hospede')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quartos.quarto')),
            ],
        ),
    ]
