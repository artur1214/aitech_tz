from django.urls import path
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, \
    SpectacularRedocView

from core.views import UserView

LIST = {
    'get': 'list',
    'post': 'create'
}
DETAIL = {
    'delete': 'destroy',
    'get': 'retrieve',
    'patch': 'partial_update',
    'put': 'update',
}

urlpatterns = [
    path('users/', UserView.as_view(LIST)),
    path('users/<int:pk>/', UserView.as_view(DETAIL)),

]

if settings.DEBUG:
    urlpatterns += [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/swagger-ui/',
             SpectacularSwaggerView.as_view(url_name='schema'),
             name='swagger-ui'),
        path('schema/redoc/',
             SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
