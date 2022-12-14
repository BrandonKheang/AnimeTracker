# Generated by Django 4.1 on 2022-08-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_alter_anime_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
        migrations.AddField(
            model_name='review',
            name='reviewType',
            field=models.CharField(choices=[('review', 'Review'), ('vote', 'Vote')], max_length=100, null=True),
        ),
    ]
