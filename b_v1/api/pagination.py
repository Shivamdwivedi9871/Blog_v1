from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class ResultPerPage(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'end'
    max_page_size = 10


class ResultLimitOffSet(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'limit'
    offset_query_param = 'strat'


class ResultCursorPage(CursorPagination):
    page_size = 4
    cursor_query_param = 'cursor'
    ordering = 'created'


class CommentViewPage(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    page_size_query_param = 'end'
    max_page_size = 10
