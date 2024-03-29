# Generated by Django 3.2.2 on 2021-06-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=130, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
