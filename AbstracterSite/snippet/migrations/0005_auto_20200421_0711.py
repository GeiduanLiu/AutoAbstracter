# Generated by Django 3.0.4 on 2020-04-21 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0004_auto_20200421_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='max_length',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='min_length',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='num_beams',
        ),
    ]
