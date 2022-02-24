# Generated by Django 4.0.2 on 2022-02-17 09:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lang_code', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maincontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=75)),
                ('summary', models.TextField(max_length=200)),
                ('publication_date', models.DateField()),
                ('situation', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('upgrate_date', models.DateField(auto_now=True)),
                ('cont_img', models.FileField(blank=True, upload_to='static/images')),
                ('content', ckeditor.fields.RichTextField()),
                ('meta_titile', models.CharField(max_length=50)),
                ('meta_content', models.CharField(max_length=100)),
                ('meta_tag', models.CharField(max_length=50)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.category', to_field='cat_name')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.lang', to_field='lang_code')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
