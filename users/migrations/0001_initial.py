# Generated by Django 4.2.3 on 2023-07-16 06:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with this username already exists!'}, help_text='Required. max lenght is 30 characters', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_\\.]+$', 'Enter a valid username', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('phone_number', models.BigIntegerField(blank=True, error_messages={'unique': 'A user with this phone number already exists.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'Enter a valid phone number')], verbose_name='phone number')),
                ('is_staff', models.BooleanField(default=False, help_text='determines whether the user can log in to the admin site or not', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='determines whether this user should be treated as an active user or not (unselect this instead of deleting accounts)', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_seen', models.DateTimeField(null=True, verbose_name='last seen date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
            managers=[
                ('objects', users.models.Usermanager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=25, verbose_name='nick_name')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='avatar')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('gender', models.BooleanField(help_text='Female is FALSE, Male is TRUE, Null for UNSET', null=True, verbose_name='gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uuid', models.UUIDField(null=True, verbose_name='Device UUID')),
                ('last_login', models.DateTimeField(null=True, verbose_name='Last Login Date')),
                ('device_type', models.PositiveSmallIntegerField(choices=[(1, 'WEB'), (2, 'IOS'), (3, 'ANDROID')], default=1)),
                ('createdd_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
                'db_table': 'user_devices',
                'unique_together': {('user', 'device_uuid')},
            },
        ),
    ]