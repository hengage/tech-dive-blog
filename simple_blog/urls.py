from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from markdownx import urls as markdownx



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('account.urls')),

    # Password reset for admin.
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name = 'admin_password_reset'
    ),

    # markdownx 
    path('markdownx/', include(markdownx))
]


# urlpatterns += [
#     url(r'^markdownx/', include(markdownx))
# ]


handler404 = 'the_blog.views.error_404'
