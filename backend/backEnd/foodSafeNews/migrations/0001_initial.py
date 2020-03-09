# Generated by Django 3.0.3 on 2020-03-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodSafe_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=5)),
                ('news_time', models.DateField()),
                ('news_url', models.URLField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
