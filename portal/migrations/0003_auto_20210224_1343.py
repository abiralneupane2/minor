# Generated by Django 3.1.4 on 2021-02-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20210224_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='collaborators',
            field=models.ManyToManyField(null=True, related_name='collaborators', to='portal.Person'),
        ),
    ]