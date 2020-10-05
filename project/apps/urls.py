from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('django_backend_template.urls')),
    path('auth/', include('rest_auth.urls')),
]
