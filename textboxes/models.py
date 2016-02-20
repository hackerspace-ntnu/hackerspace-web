from django.db import models
from ckeditor.fields import RichTextField


class Textbox(models.Model):
    class Meta:
        verbose_name_plural = "textboxes"

    title = models.CharField(max_length=100, verbose_name='Header')
    content = RichTextField()

    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
