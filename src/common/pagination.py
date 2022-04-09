from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10000


class OrderPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = "page_size"
    max_page_size = 10000


class BlogPagination(PageNumberPagination):
    page_size = 4
    page_query_param = "page_size"
    max_page_size = 10000
