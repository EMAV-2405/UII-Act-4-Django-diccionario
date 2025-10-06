from django.urls import path
from . import views  # o desde donde importes tus vistas

urlpatterns = [
    path('', views.index, name='index.html'),
    # otras urls...
]