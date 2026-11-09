from rest_framework.pagination import PageNumberPagination


class CourseListPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = "page_size"
    max_page_size = 20


class LessonListPaginator(PageNumberPagination):
    page_size = 15
    page_query_param = "page_size"
    max_page_size = 30
