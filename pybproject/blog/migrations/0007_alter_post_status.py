# Generated by Django 4.2.1 on 2023-07-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_options_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
    ]
