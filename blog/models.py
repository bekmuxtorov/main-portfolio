from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Blog(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name = "Maqola sarlavhasi"),
        body = RichTextField(verbose_name = 'Maqola matni:'),
    )

    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(blank = True, verbose_name= "Rasm")
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