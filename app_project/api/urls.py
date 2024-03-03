from django.urls import path

from .views import (ProductLessonListView, ProductListView,
                    ProductStatusListView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/lessons/',
         ProductLessonListView.as_view(),
         name='product-lesson-list'),
    path('products_status/', ProductStatusListView.as_view(),
         name='product-status')
]