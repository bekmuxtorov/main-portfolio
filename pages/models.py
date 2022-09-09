from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from .const import Const

# Create your models here.
class Works(models.Model):
    project_directions = Const.project_directions

    img = models.ImageField(blank = True, verbose_name = "Loyiha rasmi:")
    project_name = models.CharField(max_length=50, verbose_name='Loyiha nomi:')
    project_direction = models.CharField(
        max_length=35,
        choices=project_directions,
        default=1,
        verbose_name="Loyiha yo'nalish:"

    )

    # portfolio detail
    project_short_description = models.CharField(max_length=50, verbose_name="Loyiha haqida qisqa ma'lumot:", null=True)
    project_description = RichTextField(verbose_name='Loyiha haqida(Batafsil):')

    project_date = models.DateTimeField(auto_now_add=True, null=True)
    project_client = models.CharField(max_length=30, verbose_name='Client ism:', null=True)


    project_view = models.TextField(verbose_name='Demo sayt manzili:')
    project_github = models.TextField(verbose_name="GitHub'dagi linki:")

    

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Portfolio'

    def get_direction(self):
            return dict(Works.project_directions)[self.project_direction]

    def get_date(self):
        now = self.project_date
        date_time = now.strftime("%d/%m/%Y")
        return date_time