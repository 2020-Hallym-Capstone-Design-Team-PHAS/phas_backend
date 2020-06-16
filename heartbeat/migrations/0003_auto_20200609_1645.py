# Generated by Django 3.0.7 on 2020-06-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heartbeat', '0002_heartbeat_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartbeat',
            name='audio_file_path',
        ),
        migrations.RemoveField(
            model_name='heartbeat',
            name='dog_idx',
        ),
        migrations.AddField(
            model_name='heartbeat',
            name='dog_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heartbeat',
            name='heartbeat_normal_condition',
            field=models.IntegerField(null=True),
        ),
    ]
