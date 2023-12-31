# Generated by Django 4.2.5 on 2023-09-23 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('cpf', models.CharField(max_length=11)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='TicketsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyed_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('code', models.CharField(max_length=127)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_ticket', to='tickets.ticket')),
            ],
        ),
    ]
