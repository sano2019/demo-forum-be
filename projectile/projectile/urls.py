"""projectile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

schema_view = get_schema_view(
    openapi.Info(
        title="Portal API Docs",
        default_version='v1',
        description="This documentation is for Portal",
        terms_of_service="TBD",
        contact=openapi.Contact(email="info@willandskill.se"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

admin.sites.AdminSite.site_header = 'Portal'
admin.sites.AdminSite.site_title = 'Portal'
admin.sites.AdminSite.index_title = 'Portal Admin'

auth_urls = [
    # url(
    #     r'^api/v1/auth/register/activate/',
    #     UserViewSet.activation,
    #     name='activate-user',
    # ),
    # url(
    #     r'^api/v1/auth/register/resend-activation-email/',
    #     UserViewSet.resend_activation,
    #     name='resend-activation-email',
    # ),
    # url(r'^api/v1/auth/register/', UserViewSet, name='register'),
    # url(
    #     r'^api/v1/auth/reset-password/',
    #     UserViewSet.reset_password,
    #     name='reset-password',
    # ),
    # url(
    #     r'^api/v1/auth/reset-password-confirm/',
    #     UserViewSet.reset_password_confirm,
    #     name='reset-password',
    # ),
    url(r'api/v1/auth/', include('djoser.urls')),
    url(r'^api/v1/auth/api-token-auth/', obtain_jwt_token, name='get_token'),
    url(
        r'^api/v1/auth/api-token-verify/',
        verify_jwt_token,
        name='verify_token',
    ),
]

urlpatterns = (
    [
        url(
            r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui',
        ),
        url(r'^admin/', admin.site.urls),
        url(r'^api/v1/', include('core.urls')),
        url(r'^markdownx/', include('markdownx.urls')),
        url(r'^api/v1/common/', include('common.urls')),
        url(r'^api/v1/e2eutils/', include('e2eutils.api.urls')),
        url('forum/', include('forum.urls')),
        # url(r'^api-token-refresh/', refresh_jwt_token, name='refresh_token'),
    ]
    + auth_urls
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
