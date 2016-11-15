# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('amount_float', models.FloatField()),
                ('amount_int', models.IntegerField()),
                ('date', models.DateField()),
                ('date_timed', models.DateTimeField()),
                ('choice', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Compra_Produto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='estoque.Base')),
            ],
            bases=('estoque.base', models.Model),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='estoque.Base')),
            ],
            bases=('estoque.base', models.Model),
        ),
        migrations.CreateModel(
            name='Retira_Produto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='estoque.Base')),
                ('amout_refresh', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_clinica.Funcionario')),
            ],
            bases=('estoque.base', models.Model),
        ),
        migrations.AddField(
            model_name='compra_produto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto'),
        ),
    ]
