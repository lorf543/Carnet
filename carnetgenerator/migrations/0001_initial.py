# Generated by Django 5.0.6 on 2024-06-14 03:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(upload_to='profile_picture')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
                ('id_carnet', models.CharField(blank=True, max_length=50, null=True)),
                ('employee_status', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=50)),
                ('carnet_status', models.CharField(blank=True, max_length=50, null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_code')),
                ('identification', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('eyes', models.CharField(max_length=50)),
                ('skin', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('blood_type', models.CharField(max_length=50)),
                ('num_print', models.IntegerField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
