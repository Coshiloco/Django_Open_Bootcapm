# Generated by Django 4.0.5 on 2022-07-22 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0007_coments_dia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Coment',
        ),
    ]
