# Generated by Django 3.2.5 on 2021-07-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_one', models.ImageField(upload_to=None)),
                ('image_two', models.ImageField(upload_to=None)),
                ('blurb', models.CharField(max_length=100)),
            ],
        ),
    ]
