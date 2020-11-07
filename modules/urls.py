from django.urls import path

from modules.views import ModuleDetail, ModuleList, addStudents

urlpatterns = [
    path('modules', ModuleList.as_view()),
    path('modules/<str:pk>', ModuleDetail.as_view()),
    path('modules/<str:pk>/add_students', addStudents)
]