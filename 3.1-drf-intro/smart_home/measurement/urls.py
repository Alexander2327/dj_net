from django.urls import path
from .views import SensorDetailView, SensorsView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
]
