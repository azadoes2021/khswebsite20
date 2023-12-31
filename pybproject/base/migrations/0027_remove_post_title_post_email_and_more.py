# Generated by Django 4.2.1 on 2023-07-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_post_terms_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='post',
            name='terms_confirmed',
            field=models.BooleanField(max_length=10, null=True, verbose_name='개인정보 수집 동의'),
        ),
    ]
