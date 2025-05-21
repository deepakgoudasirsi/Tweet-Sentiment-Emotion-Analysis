from django.urls import path
from . import views

app_name = 'emotion'

urlpatterns = [
    path('', views.emotion_analysis, name="emotion_analysis"),  # For the home page
    path('type/', views.emotion_analysis_type, name="emotion_analysis_type"),  # For the typed tweet analysis
    path('import/', views.emotion_analysis_import, name="emotion_analysis_import"),  # For the imported tweet analysis
]
