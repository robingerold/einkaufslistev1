from django.urls import path
from . import views

urlpatterns = [
    path('', views.updates),
    path('shoppinglist/', views.shoppinglist),
    path('feedback/', views.feedback),


]