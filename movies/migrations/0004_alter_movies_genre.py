# Generated by Django 4.1.2 on 2022-11-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Aventure', 'Aventure'), ('Comedie', 'Comedie'), ('Drame', 'Drame'), ('Fantastique', 'Fantastique'), ('Horreur', 'Horreur'), ('Policier', 'Policier'), ('Science-fiction', 'Science-fiction'), ('Thriller', 'Thriller'), ('Adulte', 'Adulte')], max_length=255),
        ),
    ]
