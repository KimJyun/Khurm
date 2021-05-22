# Generated by Django 3.2 on 2021-05-22 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import folder.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('f_no', models.AutoField(primary_key=True, serialize=False, verbose_name='파일번호')),
                ('title', models.CharField(db_column='f_name', default='default', max_length=30, verbose_name='파일 이름')),
                ('file_path', models.CharField(default='.', max_length=200, verbose_name='파일절대경로')),
                ('file_type', models.CharField(default='None', max_length=20, verbose_name='파일 타입')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='파일 생성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='파일 최근 수정일')),
                ('f_size', models.IntegerField(default=0, verbose_name='파일용량')),
                ('f_tag', models.CharField(default='None', max_length=200, verbose_name='남녀명수')),
                ('file', models.FileField(default='media/test.txt', upload_to=folder.models.get_upload_path)),
                ('owner', models.ForeignKey(db_column='f_owner', on_delete=django.db.models.deletion.CASCADE, related_name='file', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Files',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth', models.CharField(default='R', max_length=100, verbose_name='권한(R/W)')),
                ('file_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared', to='folder.file')),
                ('user_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='folder.file')),
                ('user_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
