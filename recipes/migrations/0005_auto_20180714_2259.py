# Generated by Django 2.0.7 on 2018-07-15 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20180714_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='contributor',
        ),
        migrations.DeleteModel(
            name='Contributor',
        ),
    ]
