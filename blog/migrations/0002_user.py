# Generated by Django 3.1.6 on 2021-02-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
