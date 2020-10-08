from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('produto/', include('produto.urls')),
    path('sobre/', include('sobre.urls'))
]
