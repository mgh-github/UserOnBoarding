# Generated by Django 3.1.1 on 2021-04-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_auto_20210401_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='Photo',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='user',
            name='type_of_account',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='user_account.account'),
            preserve_default=False,
        ),
    ]
