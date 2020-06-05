from django.urls import path
from register import views

urlpatterns = [
    path('register/', views.register),
    path('registration_success/', views.registration_success)

]
