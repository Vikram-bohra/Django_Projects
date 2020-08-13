from django.db import models
from datetime import datetime

class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField(default=datetime.now,blank=True)
    post_date_gmt = models.DateTimeField(default=datetime.now,blank=True)
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField(default=datetime.now,blank=True)
    post_modified_gmt = models.DateTimeField(default=datetime.now,blank=True)
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpWpdevartImages(models.Model):
    id = models.BigAutoField(unique=True,primary_key=True)
    image_h = models.TextField(blank=True, null=True)
    image_w = models.TextField(blank=True, null=True)
    image_size = models.TextField(blank=True, null=True)
    image_type = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=4048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wpdevart_images'



class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'

class Extra_image(models.Model):
    name = models.CharField(max_length= 10)
    image = models.ImageField(upload_to='images/')

class video(models.Model):
    name = models.CharField(max_length=20)
    vid = models.FileField(upload_to='videos/')

