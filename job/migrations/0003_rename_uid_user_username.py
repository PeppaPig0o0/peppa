# Generated by Django 3.2 on 2023-06-11 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20230611_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uid',
            new_name='username',
        ),
    ]