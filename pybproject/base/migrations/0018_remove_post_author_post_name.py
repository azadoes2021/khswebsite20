# Generated by Django 4.2.1 on 2023-06-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]