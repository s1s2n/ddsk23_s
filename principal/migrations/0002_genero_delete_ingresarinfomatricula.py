# Generated by Django 4.0.4 on 2022-05-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgenero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'genero',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='IngresarInfoMatricula',
        ),
    ]