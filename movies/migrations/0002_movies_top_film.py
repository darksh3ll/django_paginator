# Generated by Django 4.1.2 on 2022-10-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='top_film',
            field=models.BooleanField(default=False),
        ),
    ]
