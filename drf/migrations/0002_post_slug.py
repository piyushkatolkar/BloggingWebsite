# Generated by Django 3.2.2 on 2021-06-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]