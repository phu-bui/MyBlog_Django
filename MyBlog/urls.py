from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import user_login, user_logout
from django.conf.urls import url, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)