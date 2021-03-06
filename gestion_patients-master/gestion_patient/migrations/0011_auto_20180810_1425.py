# Generated by Django 2.1 on 2018-08-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_patient', '0010_auto_20171204_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiologue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('statut', models.CharField(choices=[('praticien clinicien', 'praticien clinicien'), ('praticien hospitalier', 'praticien hospitalier'), ('interne', 'interne')], max_length=30)),
                ('tempsDeTravail', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='demande',
            name='injection',
            field=models.CharField(choices=[('oui', 'oui'), ('non', 'non'), ('à voir', 'à voir')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demande',
            name='realisation',
            field=models.CharField(choices=[('oui', 'oui'), ('non', 'non')], default='non', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='type_examen',
            field=models.CharField(choices=[('scanner cerebral', 'scanner cerebral'), ('scanner AP', 'scanner AP'), ('scanner TAP', 'scanner TAP'), ('angioscanner pulmonaire', 'angioscanner pulmonaire'), ('uroscanner', 'uroscanner'), ('scanner Thoracique', 'scanner thoracique')], max_length=30),
        ),
    ]
