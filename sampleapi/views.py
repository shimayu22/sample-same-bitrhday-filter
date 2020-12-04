from django_filters import rest_framework as filters
from rest_framework import viewsets

from sample.models import Samplepeople
from sampleapi.serializers import SamplepeopleSerializers

class SampleFilter(filters.FilterSet):
    birthday_month = filters.NumberFilter(field_name='date_of_birth', lookup_expr='month')
    birthday_day = filters.NumberFilter(field_name='date_of_birth', lookup_expr='day')

    class Meta:
        model = Samplepeople
        fields = ['id', 'name', 'kana', 'date_of_birth',]

class SampleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Samplepeople.objects.all()
    serializer_class = SamplepeopleSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = SampleFilter
