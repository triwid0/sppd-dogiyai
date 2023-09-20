# Generated by Django 4.2.4 on 2023-09-20 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_masterpengesah_namax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterpengesah',
            name='namax',
        ),
        migrations.AddField(
            model_name='masterpengesah',
            name='idPeg',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.RESTRICT, to='main.masterpegawai'),
        ),
    ]