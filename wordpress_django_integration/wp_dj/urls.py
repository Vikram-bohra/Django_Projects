"""wp_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from wp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.demo),
    path('demo/2', views.demo2.as_view()),
    path('demo/form', views.demo3),
    path('delete/<int:pid>', views.delete),
    path('update/<int:pid>', views.update),
    path('image/', views.image),
    path('comments/', views.comments),
    path('image_view/', views.view_image),
    path('image_in/', views.in_image),
    path('image_api/', views.image_api.as_view()),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)