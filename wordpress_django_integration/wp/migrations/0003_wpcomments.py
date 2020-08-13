# Generated by Django 2.2.1 on 2019-10-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wp', '0002_wpwpdevartimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='WpComments',
            fields=[
                ('comment_id', models.BigAutoField(db_column='comment_ID', primary_key=True, serialize=False)),
                ('comment_post_id', models.BigIntegerField(db_column='comment_post_ID')),
                ('comment_author', models.TextField()),
                ('comment_author_email', models.CharField(max_length=100)),
                ('comment_author_url', models.CharField(max_length=200)),
                ('comment_author_ip', models.CharField(db_column='comment_author_IP', max_length=100)),
                ('comment_date', models.DateTimeField()),
                ('comment_date_gmt', models.DateTimeField()),
                ('comment_content', models.TextField()),
                ('comment_karma', models.IntegerField()),
                ('comment_approved', models.CharField(max_length=20)),
                ('comment_agent', models.CharField(max_length=255)),
                ('comment_type', models.CharField(max_length=20)),
                ('comment_parent', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_comments',
                'managed': False,
            },
        ),
    ]