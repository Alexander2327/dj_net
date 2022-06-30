from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFromToRangeFilter, NumberFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .permissions import UpdateDeletePermission
from .serializers import AdvertisementSerializer


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter(field_name='created_at')
    creator = NumberFilter(field_name='creator_id')

    class Meta:
        model = Advertisement
        fields = ('created_at', 'creator_id')


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["destroy", "update", "partial_update"]:
            return [UpdateDeletePermission()]
        return []
