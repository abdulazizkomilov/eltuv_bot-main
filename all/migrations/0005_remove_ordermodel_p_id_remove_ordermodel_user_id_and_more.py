# Generated by Django 4.0.2 on 2022-02-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0004_alter_korzinamodel_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='p_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='order',
            field=models.CharField(blank=True, choices=[('Kutilmoqda', 'Kutilmoqda'), ('Tasdiqlandi', 'Tasdiqlandi'), ('Yuborildi', 'Yuborildi'), ('Yetkazildi', 'Yetkazildi')], default='Kutilmoqda', max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='product',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all.telegramusermodel'),
        ),
    ]
