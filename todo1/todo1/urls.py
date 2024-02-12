
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from api import views

from rest_framework_simplejwt.views import TokenVerifyView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('task',views.TaskViewSet, basename='api')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('',include(router.urls)),
    path('userlogin/',views.UserLoginApi.as_view()),
]
urlpatterns += router.urls