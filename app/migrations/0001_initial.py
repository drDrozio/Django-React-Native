# Generated by Django 3.2.6 on 2021-08-21 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50)),
                ('publisher', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, unique=True)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('published', models.DateField(blank=True, default=None, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, upload_to='uploads/')),
                ('bookdetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.bookdetails')),
            ],
        ),
    ]
