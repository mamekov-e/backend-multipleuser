from django.urls import path
from .views import (EmployeeSignupView,
                    DirectorSignupView,
                    UserTokenObtainPairView, LogoutView, EmployeeOnlyView, DirectorOnlyView)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/employee/', EmployeeSignupView.as_view()),
    path('signup/director/', DirectorSignupView.as_view()),

    path('login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('login/', CustomAuthToken.as_view(), name='auth-token'),
    # path('logout/', LogoutView.as_view(), name='logout-view'),
    path('employee/dashboard/', EmployeeOnlyView.as_view(), name='employee-dashboard'),
    path('director/dashboard/', DirectorOnlyView.as_view(), name='director-dashboard'),
]
