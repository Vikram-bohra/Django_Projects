from rest_framework import serializers
from .models import WpPosts,Extra_image,WpWpdevartImages

class data_serializer(serializers.ModelSerializer):
    class Meta:
        model = WpPosts
        fields = ('id','post_author','post_date','post_date_gmt','post_content','post_title','post_excerpt','post_status','comment_status','ping_status','post_password','post_name','to_ping','pinged','post_modified','post_content_filtered','post_parent','menu_order','post_type','comment_count',)

class image_serializer(serializers.ModelSerializer):
    class Meta:
        model = WpWpdevartImages    #WpWpdevartImages , Extra_images ,
        fields = '__all__'
