# Generated by Django 3.2.19 on 2024-04-06 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cores', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanhos', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipos', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Uniforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uquantidade', models.IntegerField(default=0)),
                ('upreço', models.FloatField(default=0.0)),
                ('ucor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.core')),
                ('utamanho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.tamanho')),
                ('utipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.tipo')),
            ],
        ),
    ]