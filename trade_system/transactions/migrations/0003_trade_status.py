# Generated by Django 3.1.11 on 2021-06-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20210527_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'OPEN'), (2, 'CLOSE')], default=1),
        ),
    ]
