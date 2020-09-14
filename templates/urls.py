from django.urls import re_path

from templates import views

app_name = 'templates_app'

urlpatterns = [
    re_path(r'^v1/templates/$', views.TemplatesListAPI.as_view(), name='templates'),
    re_path(r'^v1/templates/(?P<template_id>[0-9a-f-]+)/$', views.GetTemplateAPI.as_view(), name='template'),
]
