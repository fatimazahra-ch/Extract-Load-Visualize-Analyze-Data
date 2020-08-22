from django.contrib import admin
from django.urls import path, include
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('recherche/', include('recherche.urls', namespace="recherche_app")),
    path('register/', include('register.urls')),
    path('logoutPage/', include('logout.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
