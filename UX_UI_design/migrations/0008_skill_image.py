# Generated by Django 4.1.5 on 2023-01-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UX_UI_design', '0007_remove_skill_skill_1_remove_skill_skill_10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/djangoProject/img'),
        ),
    ]