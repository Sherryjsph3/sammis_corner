# Generated by Django 3.2.5 on 2021-07-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_post_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blurb',
            field=models.TextField(),
        ),
    ]
