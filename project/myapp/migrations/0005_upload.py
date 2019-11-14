# Generated by Django 2.2.5 on 2019-11-08 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_registr'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='image/')),
                ('fk_login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Login')),
            ],
        ),
    ]
