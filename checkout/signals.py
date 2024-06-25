from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
if were not seeing order totals in order admin this could be here: 
"""
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print("Delete signal recieved")
    instance.order.update_total()