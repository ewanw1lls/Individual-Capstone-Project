# Generated by Django 4.2.20 on 2025-03-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='field_type',
            field=models.CharField(
                choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')],
                default='Outdoor',
                max_length=7
            ),
        ),
    ]
