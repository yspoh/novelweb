from  django.urls import path

from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    # path('rank/', views.rank, name='rank'),
    # path('user/', views.user, name='user'),
    # path('', views.xuanhuan, name='xuanhuan'),
]