# Generated by Django 4.1 on 2022-08-16 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profile_image'),
        ('animes', '0002_rename_default_image_anime_featured_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'anime')},
        ),
    ]
