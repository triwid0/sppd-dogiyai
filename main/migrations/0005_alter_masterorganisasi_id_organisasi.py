# Generated by Django 4.2.5 on 2023-09-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_masterjabatan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterorganisasi',
            name='id_organisasi',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
