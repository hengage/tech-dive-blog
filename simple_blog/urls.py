from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 

from markdownx import urls as markdownx



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('accounts/', include('allauth.urls')),

    # Password reset for admin.
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name = 'admin_password_reset'
    ),

    # markdownx 
    path('markdownx/', include(markdownx))
    # path('markdownx/', include('markdownx.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [
#     url(r'^markdownx/', include(markdownx))
# ]


handler404 = 'the_blog.views.error_404'
