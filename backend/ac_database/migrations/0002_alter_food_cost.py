# Generated by Django 4.0.1 on 2022-02-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='cost',
            field=models.FloatField(),
        ),
    ]