from django.conf.urls import url

from .views import (
    RemoveRegistrationAccount,
    CreateTestAccount,
    ResetPasswordLink,
)

app_name = 'e2eutils'
urlpatterns = [
    url(
        r'^remove-registration-account/$',
        RemoveRegistrationAccount.as_view(),
        name='remove-registration-account',
    ),
    url(
        r'^create-test-account/$',
        CreateTestAccount.as_view(),
        name='create-test-account',
    ),
    url(
        r'^reset-password-link/$',
        ResetPasswordLink.as_view(),
        name="reset-password-link",
    ),
]
