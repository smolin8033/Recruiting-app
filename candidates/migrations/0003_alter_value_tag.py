# Generated by Django 4.0.4 on 2022-05-19 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_tag_candidate_alter_value_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='candidates.tag'),
        ),
    ]
