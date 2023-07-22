from django.urls import path
from .import views
app_name = "My_app"
urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('result/', views.view_result, name='result'),
    ]