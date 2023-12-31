# Generated by Django 4.2.2 on 2023-06-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permuta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('tipo', models.CharField(choices=[('n', 'Noturna'), ('f', 'FDS'), ('s', 'Semanal')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id_roteiro', models.IntegerField(primary_key=True, serialize=False)),
                ('posto_base', models.CharField(max_length=25)),
                ('area_semanal', models.CharField(max_length=20)),
                ('area_fds', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('mat', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tp_semanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('m', 'Matutino'), ('v', 'Vespertino')], max_length=1)),
                ('fk_permuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.permuta')),
                ('roteiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.roteiro')),
            ],
        ),
        migrations.CreateModel(
            name='Tp_noturno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(choices=[('a', 'Noturno-A'), ('b', 'Noturno-B'), ('c', 'Noturno-C')], max_length=2)),
                ('fk_permuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.permuta')),
            ],
        ),
        migrations.CreateModel(
            name='Tp_fds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(choices=[('i', 'I'), ('ii', 'II'), ('iii', 'III'), ('iv', 'IV'), ('v', 'V')], max_length=3)),
                ('fk_permuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.permuta')),
                ('roteiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.roteiro')),
            ],
        ),
        migrations.AddField(
            model_name='permuta',
            name='fk_escalado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escalado', to='sefit.servidor'),
        ),
        migrations.AddField(
            model_name='permuta',
            name='fk_substituto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substituto', to='sefit.servidor'),
        ),
        migrations.CreateModel(
            name='Afastamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('motivo', models.CharField(max_length=10)),
                ('obs', models.TextField(max_length=120, null=True)),
                ('fk_servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sefit.servidor')),
            ],
        ),
    ]
