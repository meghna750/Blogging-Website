# Generated by Django 3.2.4 on 2021-06-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
