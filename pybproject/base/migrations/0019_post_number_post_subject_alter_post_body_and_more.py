# Generated by Django 4.2.1 on 2023-07-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_remove_post_author_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.CharField(max_length=50, null=True, verbose_name='전화번호'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(choices=[('세무기장 서비스', '세무기장 서비스'), ('경리 아웃소싱', '경리 아웃소싱'), ('재산세신고', '재산세신고'), ('세무자문 서비스', '세무자문 서비스'), ('경정청구 서비스', '경정청구 서비스'), ('기타', '기타')], default='', max_length=50, verbose_name='문의종류'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='성함'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]