# Generated by Django 4.0.4 on 2022-10-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Recolector'), (2, 'AdminFinca'), (3, 'Operador'), (4, 'AdminEmpresa')], default=1),
        ),
    ]