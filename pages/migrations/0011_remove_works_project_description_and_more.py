# Generated by Django 4.0.6 on 2022-11-27 15:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_home_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='project_description',
        ),
        migrations.RemoveField(
            model_name='works',
            name='project_short_description',
        ),
        migrations.CreateModel(
            name='WorksTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('project_short_description', models.CharField(max_length=50, null=True, verbose_name="Loyiha haqida qisqa ma'lumot:")),
                ('project_description', ckeditor.fields.RichTextField(verbose_name='Loyiha haqida(Batafsil):')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='pages.works')),
            ],
            options={
                'verbose_name': 'Portfolio Translation',
                'db_table': 'pages_works_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model) 
        ),
    ]
