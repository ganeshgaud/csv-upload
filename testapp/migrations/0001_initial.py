# Generated by Django 2.2 on 2020-03-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('college_name', models.CharField(max_length=64)),
                ('std_cell_no', models.BigIntegerField()),
                ('emai_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
