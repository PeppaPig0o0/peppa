# Generated by Django 3.2 on 2023-04-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='学生姓名', max_length=255, verbose_name='姓名')),
                ('age', models.IntegerField(help_text='年龄', max_length=10, verbose_name='年龄')),
                ('gender', models.CharField(choices=[(1, '男'), (0, '女')], max_length=5, verbose_name='性别')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'ordering': ('name',),
            },
        ),
    ]