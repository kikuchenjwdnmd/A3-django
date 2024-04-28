# Generated by Django 5.0.4 on 2024-04-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNo', models.CharField(max_length=10)),
                ('departure', models.CharField(max_length=5)),
                ('departureCityName', models.CharField(max_length=50)),
                ('departureFullName', models.CharField(max_length=100)),
                ('arrive', models.CharField(max_length=5)),
                ('arriveCityName', models.CharField(max_length=50)),
                ('arriveFullName', models.CharField(max_length=100)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit', models.CharField(max_length=4)),
                ('operated', models.CharField(max_length=100)),
                ('airlines', models.CharField(max_length=50)),
                ('imageUrl', models.CharField(max_length=200)),
                ('aircraft', models.CharField(max_length=50)),
                ('luggageFree', models.CharField(max_length=10)),
                ('flightTime', models.CharField(max_length=10)),
                ('nonStop', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='user_id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=32),
        ),
    ]