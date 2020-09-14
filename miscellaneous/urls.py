from django.urls import path

from .views import MiscellaneousFeatures

app_name = "miscellaneous"

urlpatterns = [
    path('v1/miscellaneous/', MiscellaneousFeatures.as_view(), name='miscellaneous'),
    path('v1/miscellaneous/<str:slug>/', MiscellaneousFeatures.as_view(), name='miscellaneous'),
]
