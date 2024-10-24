from .views import SignupView, LogoutView, CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
