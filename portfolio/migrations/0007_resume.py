# Generated by Django 3.0 on 2021-01-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_about_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('cv_file', models.FileField(upload_to='document')),
            ],
        ),
    ]
