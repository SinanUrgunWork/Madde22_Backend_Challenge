# Generated by Django 4.0.4 on 2023-08-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('brewery_type', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_2', models.CharField(blank=True, max_length=200, null=True)),
                ('address_3', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state_province', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('users_interacted', models.ManyToManyField(related_name='interacted_breweries', to='breweries.userprofile')),
            ],
        ),
    ]