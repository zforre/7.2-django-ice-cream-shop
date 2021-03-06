# Generated by Django 3.0.3 on 2020-02-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20200218_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icecream',
            options={'ordering': ['flavor']},
        ),
        migrations.AddField(
            model_name='icecream',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='available',
            field=models.CharField(choices=[('DAILY', 'daily'), ('WEEKLY', 'weekly'), ('SEASONAL', 'seasonal')], default='daily', max_length=20),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='base',
            field=models.CharField(choices=[('choc', 'CHOCOLATE'), ('van', 'VANILLA')], default='vanilla', max_length=20),
        ),
    ]
