# Generated by Django 3.1.4 on 2021-04-04 11:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysevr', '0006_auto_20210404_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcecode',
            name='files',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=''), size=None), size=None),
        ),
    ]