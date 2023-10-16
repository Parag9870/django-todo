from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.index, name ="list"),
    path('update_task/<str:pk>/', views.updateTask, name ="update_task"),
    path('del/<str:pk>/', views.deleteTask, name ="delete")


]
