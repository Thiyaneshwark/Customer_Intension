from customerIntension.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    path('result',views.predict,name='result')
]
