# Generated by Django 2.0.13 on 2019-05-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.CharField(choices=[('T', 'Tunis'), ('N', 'Nabeul'), ('A', 'Ariana')], default=1, max_length=128),
            preserve_default=False,
        ),
    ]
