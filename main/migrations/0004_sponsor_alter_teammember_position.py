# Generated by Django 4.0.4 on 2024-06-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_teammember_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationName', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('tier', models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='teammember',
            name='position',
            field=models.CharField(default='General', max_length=100),
        ),
    ]
