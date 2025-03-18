# Generated by Django 5.1.7 on 2025-03-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=30)),
                ('date_of_birth', models.DateField(default='2000-01-01')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Unknown', max_length=1)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
