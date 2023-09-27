from django.urls import path
from . import views

urlpatterns = [
    path('', views.DevlogList.as_view(), name='home'),
    path('<slug:slug>/', views.DevlogDetail.as_view(), name='devlog_detail'),
]
