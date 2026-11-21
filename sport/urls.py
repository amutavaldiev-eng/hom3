from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('matches/', views.matches, name='matches'),
    path('', views.register, name='register'),
    path('login/', views.loginn, name='loginn'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout_user'),
    path('game/<int:id>/', views.game_see, name='game_see'),
    path('order/<int:id>/', views.order_ticket, name='order_ticket'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('cancel-order/<int:id>/', views.cancel_order, name='cancel_order'),
]