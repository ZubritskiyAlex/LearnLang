# Generated by Django 3.1.7 on 2021-04-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='question',
            name='number_true_answer',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_id',
            field=models.ManyToManyField(to='polls.Answer'),
        ),
    ]