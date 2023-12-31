# Generated by Django 4.1.3 on 2023-07-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans'), ('Prefer not to say', 'Prefer not to say')], max_length=30)),
                ('Contact_no', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Image', models.ImageField(blank=True, upload_to='Imagecontant')),
                ('Document', models.FileField(blank=True, upload_to='DocsContant')),
            ],
        ),
    ]
