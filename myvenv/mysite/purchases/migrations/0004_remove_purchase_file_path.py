# Generated by Django 2.0.2 on 2018-02-03 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_auto_20180203_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='file_path',
        ),
    ]
