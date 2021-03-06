# Generated by Django 3.2.12 on 2022-04-01 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detections', '0007_alter_detection_blob_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlinkDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blob_data', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Detection',
            new_name='NeckDetection',
        ),
    ]
