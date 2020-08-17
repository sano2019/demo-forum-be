import logging
from decimal import Decimal

from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q

from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, generics, status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from reversion.views import RevisionMixin

from common.helpers.pagination import LargeResultsSetPagination, ZeroResultsSetPagination
from common.views import EnumView

from core.models import (
    User,
)

from core.serializers import (
    MeSerializer,
)

logger = logging.getLogger(__name__)


class Me(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.none()
    serializer_class = MeSerializer

    def get_object(self):
        user = self.request.user
        return user

    # def put(self, request):
    #     serializer = MeSerializer(request.user, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    # def patch(self, request):
    #     serializer = MeSerializer(
    #         request.user, data=request.data, partial=True
    #     )
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
