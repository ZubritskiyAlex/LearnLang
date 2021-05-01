# Generated by Django 3.1.7 on 2021-04-03 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('theme', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('time_end', models.DateTimeField()),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hw_who', to='user.customer')),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hw_whom', to='user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MarkHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveSmallIntegerField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homework')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mark_who', to='user.customer')),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mark_whom', to='user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=1000, verbose_name='Comment')),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homework')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homework')),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.markhomework')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_who', to='user.customer')),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_whom', to='user.customer')),
            ],
        ),
    ]