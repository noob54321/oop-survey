# Generated by Django 2.2.2 on 2019-12-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20191209_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='state',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
