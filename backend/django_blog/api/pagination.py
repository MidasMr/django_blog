from rest_framework.pagination import PageNumberPagination


class PageNumberLimitPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
