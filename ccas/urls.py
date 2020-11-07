from django.urls import path

from ccas.views import CCADetail, CCAList

urlpatterns = [
    path('ccas', CCAList.as_view()),
    path('ccas/<str:pk>', CCADetail.as_view())
]