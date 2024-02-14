# solarpanel_project/urls.py

from django.contrib import admin
from django.urls import path, include  # include is used for including app URL configs
from django.conf import settings  # settings should be imported to access your settings
from django.conf.urls.static import static  # static is used to serve media files in development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solarpanel_checker.urls')),  # Include your app's URLs
]

# This is correct; it appends the media URL patterns to urlpatterns if DEBUG is True.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
