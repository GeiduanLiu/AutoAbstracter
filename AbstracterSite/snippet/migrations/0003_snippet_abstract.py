# Generated by Django 3.0.4 on 2020-04-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_auto_20200407_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='abstract',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
