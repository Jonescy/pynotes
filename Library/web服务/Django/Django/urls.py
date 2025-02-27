"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from apps.users import views
from django.urls.resolvers import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # u前缀的路由分发到users中
    path("u/", include("apps.users.urls"), name="users"),
    path("a/", include("apps.article.urls"), name="books"),
    path("", views.index, name="index"),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}, name="media"),  # 暴露media接口

]
