# Generated by Django 3.2.22 on 2023-10-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0011_rename_document_content_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video',
            field=models.FileField(blank=True, upload_to='DocsContant'),
        ),
    ]