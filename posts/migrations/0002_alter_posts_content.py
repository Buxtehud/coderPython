# Generated by Django 4.0.3 on 2022-03-31 05:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
