# Generated by Django 3.0.5 on 2020-05-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qas_system', '0004_tipoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='college',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='学院'),
        ),
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.TextField(blank=True, default='', max_length=20, null=True, verbose_name='年级'),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='专业'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='联系方式'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='性别'),
        ),
    ]
