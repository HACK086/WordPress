# Generated by Django 4.1.3 on 2023-04-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]