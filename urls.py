from django.urls import path
from core import views

urlpatterns = [
    path('',views.simulate_profit_loss,name='index'),
    path('dashboard/', views.create_user_dashboard,name='dash'),
    path('useradmin/', views.create_user_dashboard,name='uadmin')
]