from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import ProfessorViewSet, StudentViewSet

auth_router = routers.SimpleRouter()
auth_router.register('auth/users/professors', ProfessorViewSet, basename="professors")
auth_router.register('auth/users/students', StudentViewSet, basename="students")

jwt_urlpatterns = [
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = []

urlpatterns += jwt_urlpatterns

urlpatterns += auth_router.urls
