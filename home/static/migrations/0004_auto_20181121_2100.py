# Generated by Django 2.1.1 on 2018-11-22 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181121_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell_phone',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_phone',
            field=models.CharField(max_length=14),
        ),
    ]
