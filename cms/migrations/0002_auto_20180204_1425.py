# Generated by Django 2.0.2 on 2018-02-04 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, verbose_name='みだし')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='ありか')),
                ('description', models.TextField(blank=True, verbose_name='おまけ')),
                ('image', models.ImageField(blank=True, height_field=90, upload_to='', verbose_name='さしえ', width_field=160)),
                ('parent', models.ManyToManyField(blank=True, related_name='_contents_parent_+', to='cms.Contents', verbose_name='そろえ')),
            ],
        ),
        migrations.RemoveField(
            model_name='tsubu',
            name='parent',
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Contents', verbose_name='かんじ'),
        ),
        migrations.DeleteModel(
            name='Tsubu',
        ),
    ]
