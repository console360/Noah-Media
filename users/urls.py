from django.urls import re_path

from users import views

app_name = 'users_app'

urlpatterns = [
    re_path(r'^v1/signup/$', views.UserSignup.as_view(), name='sign_up'),
    re_path(r'^v1/signin/$', views.UserSignIn.as_view(), name='sign_in'),
    re_path(r'^v1/logout/$', views.UserLogout.as_view(), name='sign_out'),
    re_path(r'^v1/users/(?P<user_id>[0-9]+)/$', views.UserProfileAPI.as_view(), name='user_profile'),
    re_path(r'^v1/recover/$', views.UserForgotPasswordAPI.as_view(), name='forgot_password'),
]
