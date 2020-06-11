# Generated by Django 3.0.6 on 2020-06-11 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20200609_1758'),
        ('student', '0007_auto_20200609_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examname', models.CharField(max_length=100)),
                ('qpaper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Question_Paper')),
                ('questions', models.ManyToManyField(to='student.Stu_Question')),
                ('student', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exams', models.ManyToManyField(to='student.Exam_DB')),
                ('student', models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
