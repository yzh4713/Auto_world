# Generated by Django 3.0.7 on 2020-07-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('passworld', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('createtime', models.DateTimeField()),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('upusername', models.CharField(max_length=50)),
            ],
        ),
    ]
