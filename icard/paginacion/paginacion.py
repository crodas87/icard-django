from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    print('Hola amigos')

    # Tamaño de página predeterminado
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        page_size = self.get_page_size(self.request)
        return self.get_response(self.page.number, self.page.paginator.num_pages, page_size, data)

    def get_response(self, current_page, total_pages, page_size, data):
        print('entro en get_response')
        return Response({
            'current_page': current_page,
            'total_pages': total_pages,
            'page_size': page_size,
            'count': self.page.paginator.count,
            'results': data
        })
