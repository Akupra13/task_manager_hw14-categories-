from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Кастом
class CategoryPagination(PageNumberPagination):
    page_size = 5  # кол-во элементов на странице для категорий

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['name']  #по имени категории
    search_fields = ['name']  #по имени категории
    ordering_fields = ['created_at']  #по дате создания
    ordering = ['created_at']
    # Кастомный подсчета количества задач
    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        """
        Кастомный метод для подсчета количества задач, связанных с категорией.
        """
        category = self.get_object()  # Получаем категорию по pk
        task_count = category.task_set.count()  # Подсчет задач
        return Response({'task_count': task_count})  # Возвращаем результат в формате JSON
