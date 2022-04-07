# Generated by Django 3.2.12 on 2022-04-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220401_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('confirmed', 'confirmed'), ('assigned', 'assigned'), ('in_process', 'in_process'), ('done', 'done')], default='new', max_length=25),
        ),
    ]