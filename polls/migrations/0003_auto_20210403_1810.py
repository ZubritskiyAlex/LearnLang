# Generated by Django 3.1.7 on 2021-04-03 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('polls', '0002_auto_20210403_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='amount_question',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MarkPolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveSmallIntegerField()),
                ('percent_mark', models.FloatField()),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.test')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer')),
            ],
        ),
    ]
