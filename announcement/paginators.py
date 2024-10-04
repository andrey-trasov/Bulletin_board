from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
   page_size = 4    # количество сущностей на 1 странице
   page_size_query_param = 'page_size'    # количество выведенных записей
   max_page_size = 4    # максимальное количество сущностей на 1 странице