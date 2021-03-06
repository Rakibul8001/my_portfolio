# Generated by Django 3.0 on 2021-01-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
