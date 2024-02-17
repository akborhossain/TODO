from rest_framework.pagination import PageNumberPagination



class MyPagination(PageNumberPagination):
    page_size=3
    page_query_param='p'
    page_size_query_param='records'
    #max_page_size=10
    #last_page_strings='end'