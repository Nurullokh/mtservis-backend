# Generated by Django 3.2.12 on 2022-04-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_icon_servicetype_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='order_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicetype',
            name='order_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
