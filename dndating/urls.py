from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('info_user/', views.info_user, name="info"),
    path('edit_info/<info_id>', views.edit_info, name="edit"),
    path('show_profile/<info_id>', views.show_profile, name="show"),
    path('close_profile/<info_id>', views.close_profile, name="close"),
    path('search_players', views.search_players, name="search"),
    
]