# Generated by Django 4.0.6 on 2022-09-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_works_project_tech_works_project_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='project_direction',
            field=models.CharField(choices=[('1', 'Barchasi'), ('2', 'Frontend'), ('3', 'Backend'), ('4', 'Telegram bot')], default=1, max_length=35, verbose_name="Loyiha yo'nalish:"),
        ),
        migrations.AlterField(
            model_name='works',
            name='project_name',
            field=models.CharField(max_length=100, verbose_name='Loyiha nomi:'),
        ),
    ]
