# Generated by Django 2.2.2 on 2019-11-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='question_2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personality',
            name='question_3',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
