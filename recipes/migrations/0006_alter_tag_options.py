# Generated by Django 3.2.3 on 2021-05-18 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180714_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',)},
        ),
    ]
