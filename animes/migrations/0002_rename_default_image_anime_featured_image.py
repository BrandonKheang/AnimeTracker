# Generated by Django 4.1 on 2022-08-11 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='default_image',
            new_name='featured_image',
        ),
    ]