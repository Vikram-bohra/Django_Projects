from django import forms
from .models import WpPosts,Extra_image,video
from django.forms import ModelForm

class put_form(forms.ModelForm):
    class Meta:
        model = WpPosts
        fields = ('post_author','post_content','post_title','post_excerpt','post_status','comment_status','ping_status','post_password','post_name','to_ping','pinged','post_content_filtered','post_parent','menu_order','post_type','comment_count',)


class update_form(forms.ModelForm):
    class Meta:
        model = WpPosts
        fields = ('post_author','post_content','post_title','post_excerpt','post_status','comment_status','ping_status','post_password','post_name','to_ping','pinged','post_content_filtered','post_parent','menu_order','post_type','comment_count',)


class ImageForm(forms.ModelForm):
    class Meta:
        model= Extra_image
        fields= ("name", "image")

class videoform(forms.ModelForm):
    class Meta:
        model= video
        fields= ("name", "vid")