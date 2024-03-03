from django.db.models import Count, F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from product.models import Group, ProductAccess


@receiver(post_save, sender=ProductAccess)
def distribution_users(sender, instance, created, **kwargs):
    product = instance.product
    if created:
        if instance.is_paid == True and product.date_start > timezone.now():
            user = instance.user
            group = product.groups.annotate(count=Count('students')).filter(
                count__lt=F('max_users')).order_by('count').first()
            if group:
                group.students.add(user)
                return group
            else:
                new_group = Group.objects.create(
                    name=f"Группа для {product.name}",
                    product=product,
                    min_users=1,
                    max_users=5
                )
                new_group.users.add(user)
                return new_group
        elif product.date_start > timezone.now():
            print('Продукт уже начался, распределение по группам невозможно.')
        elif instance.is_paid == False:
            print('Отсутствует доступ к продукту.')
