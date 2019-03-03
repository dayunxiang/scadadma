# Generated by Django 2.0 on 2018-11-14 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entm', '0004_auto_20181114_0953'),
        ('gis', '0002_fenceshape'),
    ]

    operations = [
        migrations.AddField(
            model_name='fencedistrict',
            name='belongto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entm.Organizations'),
        ),
        migrations.AddField(
            model_name='fenceshape',
            name='administrativeLngLat',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
