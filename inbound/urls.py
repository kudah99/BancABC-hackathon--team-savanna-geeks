from django.urls import path
from inbound import views

urlpatterns = [
    path('msg/inbound/', views.inbound),
]