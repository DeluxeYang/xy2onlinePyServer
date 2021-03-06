"""xy2onlineServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from resource.views.data_import import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_import/character/', character_import),
    path('data_import/monster/', monster_import),
    path('data_import/shape/', shape_import),
    path('data_import/symbolic_animal/', symbolic_animal_import),

    path('data_import/task/', task),
    path('data_import/wdf/', wdf_import),
    path('data_import/get_was_list/', get_was_list),
]
