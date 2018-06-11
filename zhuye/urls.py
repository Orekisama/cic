from django.urls import path
from . import views

app_name = 'zhuye'
urlpatterns = [
	path('ip/', views.get_ip, name='ip')
]
