from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('transcribe/', include('transcriber.urls')),
    path('suggest-titles/', include('blog_title_suggester.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)