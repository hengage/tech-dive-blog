from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


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

    # path('^markdown/', include( 'django_markdown.urls')),


]



handler404 = 'the_blog.views.error_404'
