from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# ПРИНУДИТЕЛЬНАЯ ПЕРЕЗАГРУЗКА (убедитесь, что маршруты загружены)
print("✅ URL-адреса загружены!")
