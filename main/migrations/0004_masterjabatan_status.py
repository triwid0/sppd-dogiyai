# Generated by Django 4.2.5 on 2023-09-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_masterjabatan_masterkegiatan_masterlokasi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterjabatan',
            name='status',
            field=models.BooleanField(default=False, max_length=1),
        ),
    ]
