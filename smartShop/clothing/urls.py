from django.urls import include, path, re_path
from . import views

urlpatterns = [


    #/clothing/
    path('', views.index, name='index'),

    #/clothing/712/
    re_path(r'^(?P<clothing_id>[0-9]+)/$', views.detail, name='detail')
]