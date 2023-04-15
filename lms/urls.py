from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from courses.views import UserRegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('api-auth/', obtain_jwt_token),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
]
