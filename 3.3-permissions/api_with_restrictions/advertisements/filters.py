from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, NumberFilter

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter(field_name='created_at')
    creator = NumberFilter(field_name='creator_id')

    class Meta:
        model = Advertisement
        fields = ('created_at', 'creator_id')
