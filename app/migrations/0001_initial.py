# Generated by Django 3.2.8 on 2021-11-12 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('tell', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=1000)),
                ('pation_date', models.DateTimeField(blank=True, null=True)),
                ('doctor_date', models.DateTimeField(blank=True, null=True)),
                ('acsepted', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.login')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acsepted', models.BooleanField(default=False)),
                ('message', models.TextField(max_length=1000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.login')),
                ('pation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pation')),
            ],
        ),
    ]
