# Generated by Django 4.2.5 on 2023-09-25 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='benefits',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='commonQuestions',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='cultureFit',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='helpfulLinks',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='questionsToAsk',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='softSkills',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='technicalSkills',
        ),
    ]
