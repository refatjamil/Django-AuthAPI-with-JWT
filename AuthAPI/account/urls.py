from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('profile/', views.UserProfile.as_view()),
    path('changepass/', views.UserChangePassword.as_view()),
    path('send-email-rest-password/', views.SendPasswordResetEmail.as_view()),
    path('rest-password/<uid>/<token>/', views.UserPasswordReset.as_view()),



]
