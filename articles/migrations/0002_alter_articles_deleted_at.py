# Generated by Django 4.2.7 on 2023-11-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
