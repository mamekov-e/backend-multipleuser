from django.urls import path
from .views import (EmployeeSignupView,
                    DirectorSignupView,
                    CustomAuthToken, LogoutView, EmployeeOnlyView, DirectorOnlyView)

urlpatterns = [
    path('signup/employee/', EmployeeSignupView.as_view()),
    path('signup/director/', DirectorSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('employee/dashboard/', EmployeeOnlyView.as_view(), name='employee-dashboard'),
    path('director/dashboard/', DirectorOnlyView.as_view(), name='director-dashboard'),
]
