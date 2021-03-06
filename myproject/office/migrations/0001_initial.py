# Generated by Django 2.2.5 on 2019-10-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mostwanted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('crime_type', models.CharField(max_length=15)),
                ('crime_area', models.CharField(max_length=20)),
                ('victim', models.CharField(max_length=20)),
                ('crime_spot', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/%y/%m/%d/')),
            ],
        ),
    ]
