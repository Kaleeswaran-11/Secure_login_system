from django.urls import path
from .views import home, register_view, dashboard_view, logout_view, CustomLoginView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
