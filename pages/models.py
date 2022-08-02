from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Works(models.Model):
    img = models.ImageField(blank = True, verbose_name = "Loyiha rasmi:")
    project_name = models.CharField(max_length=30, verbose_name='Loyiha nomiL:')
    project_description = RichTextField(verbose_name='Loyiha haqida qisqacha:')
    project_tech = models.TextField(verbose_name='Loyiha uchun ishlatilgan texnalogiyalar:')
    project_view = models.TextField(verbose_name='Demo sayt manzili:')
    project_github = models.TextField(verbose_name="GitHub'dagi linki:")

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Portfolio'