from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('new_task', views.new_task, name='new_task'),
    path('new_reg', views.new_reg, name='new_reg'),
    re_path('^delete_task/(?P<pk>[0-9]+)$', views.delete_task, name='delete_task'),
    re_path('^delete_reg/(?P<pk>[0-9]+)$', views.delete_reg, name='delete_reg')
]
