# Generated by Django 2.1 on 2018-08-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_patient', '0011_auto_20180810_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiologue',
            name='nom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='radiologue',
            name='prenom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='radiologue',
            name='statut',
            field=models.CharField(choices=[('praticien clinicien', 'praticien clinicien'), ('praticien hospitalier', 'praticien hospitalier'), ('interne', 'interne')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='radiologue',
            name='tempsDeTravail',
            field=models.IntegerField(null=True),
        ),
    ]
