# Generated by Django 4.0.6 on 2022-09-08 08:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_works_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='project_short_description',
            field=models.CharField(max_length=50, null=True, verbose_name="Loyiha haqida qisqa ma'lumot:"),
        ),
        migrations.AlterField(
            model_name='works',
            name='project_description',
            field=ckeditor.fields.RichTextField(verbose_name='Loyiha haqida:'),
        ),
    ]
