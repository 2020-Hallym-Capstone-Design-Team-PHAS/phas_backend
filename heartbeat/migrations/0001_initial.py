# Generated by Django 3.0.5 on 2020-04-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heartbeat',
            fields=[
                ('audio_idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=64)),
                ('dog_idx', models.IntegerField()),
                ('audio_file_path', models.CharField(max_length=512)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('heartbeat_normal_condition', models.IntegerField()),
            ],
        ),
    ]
