# Generated by Django 4.0.5 on 2022-06-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_coments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]
