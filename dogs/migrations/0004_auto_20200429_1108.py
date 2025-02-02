# Generated by Django 2.0.13 on 2020-04-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_auto_20200429_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doginfo',
            name='dog_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='doginfo',
            name='dog_breed',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='doginfo',
            name='dog_size',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
