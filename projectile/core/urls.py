from django.conf.urls import url

from core.views import (
    Me,
)

app_name = 'core'
urlpatterns = [
    url(r'^me/$', Me.as_view(), name='me'),
]
