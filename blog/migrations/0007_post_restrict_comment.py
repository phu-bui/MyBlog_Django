# Generated by Django 3.0.4 on 2020-03-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='restrict_comment',
            field=models.BooleanField(default=False),
        ),
    ]
