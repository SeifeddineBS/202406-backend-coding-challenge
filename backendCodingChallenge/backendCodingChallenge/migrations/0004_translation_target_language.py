# Generated by Django 5.0.7 on 2024-08-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendCodingChallenge', '0003_translation_created_at_translation_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='target_language',
            field=models.CharField(default='de', max_length=3),
            preserve_default=False,
        ),
    ]
