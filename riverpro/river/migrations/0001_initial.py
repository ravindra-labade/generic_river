# Generated by Django 5.0.4 on 2024-04-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='River',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('river_name', models.CharField(max_length=20)),
                ('length', models.IntegerField()),
                ('area', models.IntegerField()),
                ('states_covered', models.CharField(max_length=20)),
                ('river_mode', models.CharField(choices=[('Perrenial', 'PERRENIAL'), ('seasonal', 'SEASONAL')], max_length=10)),
            ],
        ),
    ]