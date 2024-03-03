from django.contrib import admin

from .models import Group, Lesson, Product, ProductAccess

admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(ProductAccess)
