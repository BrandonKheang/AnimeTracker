# Generated by Django 4.1 on 2022-08-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default-profile-picture.jpg', null=True, upload_to='profiles/'),
        ),
    ]
