# Generated by Django 4.0.6 on 2022-08-02 04:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Maqola matni:'),
        ),
    ]
