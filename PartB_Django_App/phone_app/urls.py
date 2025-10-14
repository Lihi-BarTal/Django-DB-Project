from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AddApplication/', views.AddApplication, name='AddApplication'),
    path('index/', views.index, name='index'),
    path('queryResults/', views.queryResults, name='queryResults'),
    path('InstallApplication/', views.InstallApplication, name='InstallApplication'),
    path('RemoveApplication/', views.RemoveApplication, name='RemoveApplication'),

]