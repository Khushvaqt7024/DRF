import django_filters
from .models import myapp

class BookFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='published', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='published', lookup_expr='lte')

    class Meta:
        model = myapp
        fields = ['author', 'start_date', 'end_date']