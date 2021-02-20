# Generated by Django 3.1.6 on 2021-02-20 06:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210218_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('pub_date__month',)),
        ),
    ]