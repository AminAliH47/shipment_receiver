# Generated by Django 4.2.7 on 2023-11-21 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'carriers',
            },
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('tracking_number', models.CharField(max_length=10)),
                ('sender_address', models.TextField()),
                ('receiver_address', models.TextField()),
                ('status', models.CharField(choices=[('in-transit', 'In Transit'), ('inbound-scan', 'Inbound Scan'), ('delivery', 'Delivery'), ('transit', 'Transit'), ('scanned', 'Scanned')], max_length=12)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='shipments.carriers')),
            ],
            options={
                'db_table': 'shipments',
                'unique_together': {('tracking_number', 'carrier')},
            },
        ),
    ]
