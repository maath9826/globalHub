# Generated by Django 4.0.4 on 2022-06-11 16:10

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('globalHub', '0003_order_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('departureCity', models.TextField(max_length=30)),
                ('deliveryCite', models.TextField(max_length=30)),
                ('height', models.TextField(max_length=10)),
                ('width', models.TextField(max_length=10)),
                ('length', models.TextField(max_length=10)),
                ('weight', models.TextField(max_length=10)),
                ('fragile', models.BooleanField()),
                ('expressDelivery', models.BooleanField()),
                ('insurance', models.BooleanField()),
                ('packaging', models.BooleanField()),
                ('freightType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globalHub.logistics_solution')),
            ],
        ),
    ]
