from django.urls import path
from . import views

urlpatterns = [
    path('get-seismic/', views.get_seismic_data, name='get-seismic')
]
