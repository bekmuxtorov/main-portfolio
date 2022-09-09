from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Maqola sarlavhasi")
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(blank = True, verbose_name= "Rasm")
    body = RichTextField(verbose_name = 'Maqola matni:')
    blog_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def get_view(self):
        return self.blog_view
    def get_date(self):
        now = self.date
        date_time = now.strftime("%d/%m/%Y")
        return date_time