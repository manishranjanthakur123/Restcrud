# Generated by Django 2.2.3 on 2019-07-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('toy_category', models.CharField(default='', max_length=100)),
                ('release_Date', models.DateTimeField()),
                ('was_included_inhome', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
