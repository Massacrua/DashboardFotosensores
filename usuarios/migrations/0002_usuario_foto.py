# Generated by Django 4.1 on 2022-09-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/<django.db.models.fields.CharField> <django.db.models.fields.CharField>/'),
        ),
    ]
