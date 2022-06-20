from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.game_list, name='game-list'),
    path('show/<int:pk>/', views.game_detail, name='game-detail'),
    path('show/<int:pk>/delete/', views.game_delete, name='game-delete'),
    path('add/', views.game_create, name='game-create'),
    path('add2/', views.game_create, name='game-create-solo'),
]

#path('show/', views.GameListView.as_view(), name='game-list'),
#path('show/<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),
#path('show/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game-delete'),
#path('add/', views.GameCreateView.as_view(), name='game-create'),