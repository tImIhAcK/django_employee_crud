from django.contrib import admin
from django.urls import path, include
from core import settings
from django.conf.urls.static import static

urlpatterns = [
    path("employee-admin-panel/", admin.site.urls),
    path('', include('employee.urls', namespace='employee')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)