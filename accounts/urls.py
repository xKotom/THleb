from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/tags/', views.save_tags, name='save_tags'),
    path('profile/card/', views.save_card, name='save_card'),
    path('profile/event/<int:event_id>/', views.register_event, name='register_event'),
]
