from rest_framework.pagination import PageNumberPagination

class MyappPagination(PageNumberPagination):
    page_size = 5