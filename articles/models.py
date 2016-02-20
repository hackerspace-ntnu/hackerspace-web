from django.db import models
from ckeditor.fields import RichTextField

class Thumbnail(models.Model):
    image = models.ImageField(upload_to="static/thumbnails")
    title = models.CharField(max_length=100, verbose_name="Title")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    main_content = RichTextField()
    ingress_content = RichTextField()

    pub_date = models.DateTimeField('Publication date')
    thumbnail = models.OneToOneField(Thumbnail, null=True)

    def __str__(self):
        return self.title