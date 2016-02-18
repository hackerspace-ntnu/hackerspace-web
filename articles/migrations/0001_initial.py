# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_text', models.CharField(max_length=100, verbose_name='Header')),
                ('header_fontsize', models.IntegerField(default=32, verbose_name='Fontsize')),
                ('header_color', models.CharField(default='#000000', help_text='RGB-code', max_length=7, verbose_name='Color')),
                ('header_fontfamily', models.CharField(default='sans-serif', max_length=100, verbose_name='Font family')),
                ('text_text', models.TextField(max_length=10000, verbose_name='Text')),
                ('text_fontsize', models.IntegerField(default=14, verbose_name='Fontsize')),
                ('text_color', models.CharField(default='#000000', help_text='RGB-code', max_length=7, verbose_name='Color')),
                ('text_fontfamily', models.CharField(default='sans-serif', max_length=100, verbose_name='Font family')),
                ('ingress_text', models.TextField(max_length=500, verbose_name='Text')),
                ('ingress_fontsize', models.IntegerField(default=18, verbose_name='Fontsize')),
                ('ingress_color', models.CharField(default='#505050', help_text='RGB-code', max_length=7, verbose_name='Color')),
                ('ingress_fontfamily', models.CharField(default='sans-serif', max_length=100, verbose_name='Font family')),
                ('ingress_header_text', models.CharField(max_length=100, verbose_name='Header')),
                ('ingress_header_fontsize', models.IntegerField(default=24, verbose_name='Fontsize')),
                ('ingress_header_color', models.CharField(default='#505050', help_text='RGB-code', max_length=7, verbose_name='Color')),
                ('ingress_header_fontfamily', models.CharField(default='sans-serif', max_length=100, verbose_name='Font family')),
                ('pub_date', models.DateTimeField(verbose_name='Publication date')),
                ('post_type', models.IntegerField(choices=[(0, 'Article'), (1, 'Event')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_src', models.CharField(help_text='http://example.com/image.jpg', max_length=200, verbose_name='Source')),
                ('image_title', models.CharField(max_length=100, verbose_name='Title')),
                ('image_customDimensions', models.BooleanField(default=False, help_text='Uncheck if you want the original dimensions.', verbose_name='Custom dimensions')),
                ('image_width', models.IntegerField(default=200, verbose_name='Width')),
                ('image_height', models.IntegerField(default=200, verbose_name='Height')),
                ('image_float', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='Left', max_length=10, verbose_name='Float')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_image', models.ImageField(upload_to='static/thumbnails')),
                ('thumbnail_title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Thumbnail'),
        ),
    ]
