# Generated by Django 3.0.8 on 2021-02-10 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20210209_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Person')),
                ('to_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Person')),
                ('to_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Article')),
            ],
        ),
    ]