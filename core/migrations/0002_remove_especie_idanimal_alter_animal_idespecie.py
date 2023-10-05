# Generated by Django 4.2.5 on 2023-09-09 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especie',
            name='idAnimal',
        ),
        migrations.AlterField(
            model_name='animal',
            name='idEspecie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.especie'),
        ),
    ]