from rest_framework import serializers

from product.models import Group, Lesson, Product, ProductAccess, User


class LessonSerialiser(serializers.ModelSerializer):
    '''Сериализатор для урока.'''

    class Meta:
        model = Lesson
        fields= ('title', 'video_link')


class ProductSerializer(serializers.ModelSerializer):
    '''Сериализатор для продукта.'''

    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'author', 'date_create', 'date_start',
                  'price', 'lessons_count')

    def get_lessons_count(self, obj):
        return obj.lessons.count()


class ProductStatusSerializer(serializers.ModelField):
    '''Дополнительное задание. Отображение списка продуктов с дополнительной 
    информацией (Кол-во учеников занимающихся на продукте, на сколько % 
    заполнены группы, % приобретения продукта).'''

    count_stud_prod = serializers.SerializerMethodField()
    percent_fill_group = serializers.SerializerMethodField()
    percent_buy_product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'count_stud_prod', 'percent_fill_group',
                  'percent_buy_product')

    def get_count_stud_prod(self, obj):
        count_stud_prod = ProductAccess.objects.filter(
            product=obj, is_paid=True
        ).count()
        return count_stud_prod

    def get_percent_fill_group(self, obj):
        count_group = Group.objects.filter(product=obj)
        users_in_group = [group.students.count() for group in count_group]
        percent_fill = []
        if len(users_in_group) != 0:
            for i in range(len(users_in_group)):
                percent_fill.append((users_in_group[i] / obj.max_users) * 100)
        else:
            return 0
        percent_fill_group = sum(percent_fill) / len(percent_fill)
        return percent_fill_group

    def get_percent_buy_product(self, obj):
        all_users = User.objects.count()
        count_stud_prod = ProductAccess.objects.filter(
            product=obj, is_paid=True
        ).count()
        return (count_stud_prod / all_users) * 100