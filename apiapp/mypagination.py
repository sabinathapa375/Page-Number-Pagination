from rest_framework.pagination import PageNumberPagination

class MyPageNumber(PageNumberPagination):
    page_size = 7  #number of record in one page
    page_query_param = 'pg'
    page_size_query_param = 'records'
    max_page_size = 9
    last_page_strings = 'final'