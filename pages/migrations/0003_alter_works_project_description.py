# Generated by Django 4.0.6 on 2022-08-02 04:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_works_project_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='project_description',
            field=ckeditor.fields.RichTextField(verbose_name='Loyiha haqida qisqacha:'),
        ),
    ]
