# Generated by Django 4.0 on 2022-01-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above to Read Post !!', max_length=255),
        ),
    ]
