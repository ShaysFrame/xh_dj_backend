from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# this can also be in the admin.py file as well (what's the difference? idk later gotta check it out.)
admin.site.site_header  =  "Xuehanyu Admin Dashboard"  
admin.site.site_title  =  "Dashboard"
admin.site.index_title  =  "Xuehanyu Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/courses/', include('course.urls')),
    path('api/v1/activities/', include('activity.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

