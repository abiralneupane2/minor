# Generated by Django 3.0.8 on 2021-02-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_comment_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]