from django.urls import re_path

from projects import views

app_name = 'projects_app'

urlpatterns = [
    re_path(r'^v1/projects/$', views.ProjectsCreateListAPI.as_view(), name='projects'),
    re_path(r'^v1/projects/(?P<project_id>[0-9]+)/$', views.ProjectGetUpdateAPI.as_view(), name='project'),
    re_path(r'^v1/projects/(?P<project_id>[0-9]+)/parts/(?P<part_id>[0-9a-f-]+)/blocks/$',
            views.ProjectPartBlocksCreateAPI.as_view(), name='blocks'),
    re_path(r'^v1/projects/(?P<project_id>[0-9]+)/parts/(?P<part_id>[0-9a-f-]+)/blocks/(?P<block_id>[0-9a-f-]+)/$',
            views.ProjectPartBlockUpdateAPI.as_view(), name='block'),
]
