from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    This pagination style mirrors the syntax used when looking up multiple database records.
    """
    default_limit = 5
    max_limit = 10
