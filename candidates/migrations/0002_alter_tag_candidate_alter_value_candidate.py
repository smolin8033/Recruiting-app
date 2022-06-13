# Generated by Django 4.0.4 on 2022-05-19 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='candidates.candidate'),
        ),
        migrations.AlterField(
            model_name='value',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='candidates.candidate'),
        ),
    ]