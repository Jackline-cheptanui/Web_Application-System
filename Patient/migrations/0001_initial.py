# Generated by Django 4.0.6 on 2022-07-29 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_number', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('registration_date', models.DateTimeField(null=True)),
                ('first_name', models.CharField(max_length=17, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=17, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=15)),
                ('patient_visit_date', models.DateTimeField(null=True)),
                ('patient_height_in_center_metres', models.FloatField()),
                ('patient_weight_in_kg', models.FloatField()),
                ('patient_Bmi', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('patient_general_health', models.CharField(choices=[('Good', 'Good'), ('Poor', 'Poor')], max_length=17, null=True)),
                ('comments', models.CharField(max_length=500, null=True)),
                ('weight_choice', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=17)),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.patient')),
            ],
        ),
    ]
