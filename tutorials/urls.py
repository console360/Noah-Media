from django.urls import re_path

from tutorials import views

app_name = 'tutorials_app'

urlpatterns = [
    re_path(r'^v1/tutorials/$', views.TutorialsListAPI.as_view(), name='tutorials'),
    re_path(r'^v1/tutorials/(?P<tutorial_id>[0-9a-f-]+)/$', views.GetTutorialAPI.as_view(), name='tutorial'),
]
