# Generated by Django 3.2 on 2022-08-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField(blank=True, verbose_name='mensaje opcional')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
