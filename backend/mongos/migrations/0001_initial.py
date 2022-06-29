# Generated by Django 3.2.12 on 2022-04-08 08:59

from django.db import migrations, models
import djongo.models.fields
import mongos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mongo',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('test_cnt', models.IntegerField(null=True)),
                ('base64', djongo.models.fields.ArrayField(model_container=mongos.models.Blob, null=True)),
            ],
        ),
    ]