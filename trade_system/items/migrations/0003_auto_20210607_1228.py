# Generated by Django 3.1.11 on 2021-06-07 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_auto_20210527_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(related_name='inventories', to='items.Item'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='watchlists', to='items.item'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='users.user'),
        ),
        migrations.CreateModel(
            name='WatchlistSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_slots', to='items.item')),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_slots', to='items.watchlist')),
            ],
            options={
                'db_table': 'items_watchlist_items',
            },
        ),
        migrations.CreateModel(
            name='InventorySlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_slots', to='items.inventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_slots', to='items.item')),
            ],
        ),
    ]
