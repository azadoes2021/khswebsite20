# Generated by Django 4.2.1 on 2023-07-04 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_post_dbcode02'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dbcode02',
        ),
    ]
