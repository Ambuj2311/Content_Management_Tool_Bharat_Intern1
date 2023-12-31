# Generated by Django 3.2.22 on 2023-10-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0012_alter_content_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='Article',
            field=models.TextField(blank=True, default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='content',
            name='Image',
            field=models.ImageField(blank=True, default='  ', upload_to='Imagecontent'),
        ),
        migrations.AlterField(
            model_name='content',
            name='video',
            field=models.FileField(blank=True, upload_to='DocsContent'),
        ),
    ]
