# Generated by Django 3.2.6 on 2021-08-12 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_two',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.post')),
            ],
        ),
    ]
