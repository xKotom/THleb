from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_home, name='feedback_home'),
    path('complaint/', views.complaint, name='feedback_complaint'),
    path('praise/', views.praise, name='feedback_praise'),
    path('thanks/', views.thanks, name='feedback_thanks'),
]
