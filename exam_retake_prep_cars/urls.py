from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('exam_retake_prep_cars.web.urls')),
    path('profile/', include('exam_retake_prep_cars.accounts.urls')),
    path('car/', include('exam_retake_prep_cars.cars.urls')),
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
