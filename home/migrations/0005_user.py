# Generated by Django 3.1 on 2020-09-06 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200823_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='home.tasks')),
            ],
        ),
    ]
