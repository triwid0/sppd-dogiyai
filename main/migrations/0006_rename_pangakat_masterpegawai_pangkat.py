# Generated by Django 4.2.4 on 2023-09-20 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_masterorganisasi_id_organisasi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masterpegawai',
            old_name='pangakat',
            new_name='pangkat',
        ),
    ]