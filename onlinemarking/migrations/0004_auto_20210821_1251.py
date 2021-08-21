# Generated by Django 3.2.6 on 2021-08-21 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinemarking', '0003_auto_20210821_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='iteam',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='onlinemarking.category'),
        ),
    ]
