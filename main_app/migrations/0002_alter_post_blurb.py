# Generated by Django 3.2.5 on 2021-07-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blurb',
            field=models.CharField(max_length=500),
        ),
    ]
