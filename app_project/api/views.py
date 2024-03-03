from rest_framework import generics

from api.serializers import (LessonSerialiser, ProductSerializer,
                             ProductStatusSerializer)
from product.models import Lesson, Product


class ProductListView(generics.ListAPIView):
    '''Отображение основной информации о продукте и количестве уроков,
    которые принадлежат продукту.'''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductLessonListView(generics.ListAPIView):
    '''Отображение списка уроков по конкретному продукту,
    к которому пользователь имеет доступ.'''

    serializer_class = LessonSerialiser

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product=product_id)


class ProductStatusListView(generics.ListAPIView):
    '''Отображение списка продуктов с дополнительной информацией.'''

    queryset = Product.objects.all()
    serializer_class = ProductStatusSerializer