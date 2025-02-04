from django.contrib import admin
from django.urls import path, include  # ✅ ต้อง import include ด้วย

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothing_store.urls')),
]
