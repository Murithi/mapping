# Generated by Django 3.1.4 on 2020-12-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0004_auto_20201204_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionaloffice',
            name='description',
            field=models.CharField(default='Western Regional Office', max_length=50),
            preserve_default=False,
        ),
    ]
