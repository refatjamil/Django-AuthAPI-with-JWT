from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    path('api/register/', views.UserRegistrationView.as_view()),
    path('api/login/', views.UserLoginView.as_view()),
    path('api/profile/', views.UserProfile.as_view()),
    path('api/changepass/', views.UserChangePassword.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
