# Generated by Django 3.2.4 on 2021-06-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourblog', '0008_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=100),
        ),
    ]