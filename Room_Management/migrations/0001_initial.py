# Generated by Django 5.0.7 on 2024-07-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=50)),
                ('available_seat', models.IntegerField()),
                ('type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple'), ('customized', 'Customized')], max_length=20)),
                ('available_date', models.DateField(blank=True, null=True)),
                ('floor', models.IntegerField()),
            ],
        ),
    ]
