# Generated by Django 3.0.5 on 2020-05-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qas_system', '0005_auto_20200504_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='个人简历'),
        ),
    ]
