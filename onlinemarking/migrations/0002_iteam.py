# Generated by Django 3.2.6 on 2021-08-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinemarking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('image', models.CharField(max_length=1056)),
            ],
        ),
    ]
