# Generated by Django 4.0.4 on 2022-06-04 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post_image', models.ImageField(blank=True, upload_to='post_image')),
                ('category', models.CharField(blank=True, choices=[(None, 'Choose...'), ('Technology', 'Technology'), ('Software', 'Software'), ('Business', 'Business'), ('Fashion', 'Fashion'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Food', 'Food')], max_length=50, verbose_name='category')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
