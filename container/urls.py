from django.urls import path

from container import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]
