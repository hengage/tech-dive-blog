from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

# from markdownx import urls as markdownx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('account.urls')),

    # Django broswer reload
    path("__reload__/", include("django_browser_reload.urls")),

    # Django prose for text editing
    path("prose/", include("prose.urls")),

    # markdownx 
    # path('markdownx/', include(markdownx))
    # path('markdownx/', include('markdownx.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [
#     url(r'^markdownx/', include(markdownx))
# ]


handler404 = 'the_blog.views.error_404'
