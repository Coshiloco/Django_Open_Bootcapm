# Generated by Django 4.0.5 on 2022-06-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_coments_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=50)),
                ('segundoApellido', models.CharField(max_length=25)),
            ],
        ),
    ]
