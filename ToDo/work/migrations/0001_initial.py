# Generated by Django 3.2.8 on 2021-10-16 13:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('color', models.CharField(choices=[('blue', 'blue'), ('red', 'red'), ('yellow', 'yellow'), ('orange', 'orange'), ('pink', 'pink')], max_length=20, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 18, 21, 21, 55178), null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
