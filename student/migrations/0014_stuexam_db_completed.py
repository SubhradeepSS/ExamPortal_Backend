# Generated by Django 3.0.6 on 2020-06-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20200611_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuexam_db',
            name='completed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
