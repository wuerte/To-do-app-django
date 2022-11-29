from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app_to_do/', include('app_to_do.urls')),
    path('admin/', admin.site.urls),
]