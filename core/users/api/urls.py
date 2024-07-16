from django.contrib import admin
from django.urls import path
from .views import FreelanceSignupView, ClientSignupView, CustomAuthToken, LogoutView, ClientOnlyView, FreelanceOnlyView

urlpatterns = [
    path('signup/freelance/', FreelanceSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout/',LogoutView.as_view()),
    path('freelance/dashboard/',FreelanceOnlyView.as_view()),
    path('client/dashboard/',ClientOnlyView.as_view())
]