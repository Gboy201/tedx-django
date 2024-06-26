# Generated by Django 4.0.4 on 2024-06-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_sponsor_sponsorlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('pfp', models.ImageField(upload_to='images/')),
                ('intro', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.CharField(default='#', max_length=200),
        ),
    ]
