# Generated by Django 3.1.6 on 2021-05-17 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livraison',
            old_name='Materiel_id',
            new_name='Materiel',
        ),
    ]
