from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('api/', include('core.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

