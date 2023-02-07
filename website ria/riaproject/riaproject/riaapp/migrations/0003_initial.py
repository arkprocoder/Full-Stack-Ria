# Generated by Django 4.1.5 on 2023-02-07 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('riaapp', '0002_remove_album_artist_delete_person_delete_album_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=150)),
                ('courseFee', models.IntegerField()),
                ('courseDuration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('fatherName', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=14)),
                ('alternateNumber', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('collegeName', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=150)),
                ('landmark', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('companyName', models.CharField(blank=True, max_length=150, null=True)),
                ('designation', models.CharField(max_length=150)),
                ('qualification', models.CharField(max_length=100)),
                ('computerKnowledge', models.CharField(max_length=50)),
                ('Course', models.TextField(blank=True, max_length=350, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountPaid', models.IntegerField()),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(default='Unpaid', max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riaapp.register')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='documents')),
                ('verification', models.BooleanField(default=False)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riaapp.register')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ImageField(upload_to='certificates')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riaapp.register')),
            ],
        ),
    ]
