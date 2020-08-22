from django.urls import path
from . import views

app_name = 'recherche_app'

urlpatterns = [
    path('', views.recherche, name="recherche"),
    path('candidate/', views.candidate),
    path('profile/', views.profile, name="profile"),
    path('creativeTeam/', views.creativeTeam, name="creativeTeam"),
]