from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_name>/', views.get_response_by_num),
    path('<str:week_name>/', views.get_info_by_week_day, name='todo')

]
