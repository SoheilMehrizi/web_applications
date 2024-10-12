from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    # Sets How many objects will be visible in a page .
    page_size = 2
    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'all_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })