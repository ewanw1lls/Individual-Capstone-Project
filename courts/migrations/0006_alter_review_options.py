# Generated by Django 4.2.20 on 2025-03-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0005_alter_court_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_on']},
        ),
    ]
