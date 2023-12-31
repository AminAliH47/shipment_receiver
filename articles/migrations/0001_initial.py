# Generated by Django 4.2.7 on 2023-11-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sku', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
