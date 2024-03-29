# Generated by Django 4.2.5 on 2024-02-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='duriation',
            new_name='duration',
        ),
        migrations.AlterField(
            model_name='passenger',
            name='first',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='last',
            field=models.CharField(max_length=60),
        ),
    ]
