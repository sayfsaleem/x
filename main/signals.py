from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WithdrawalRequest,CustomUser

@receiver(post_save, sender=WithdrawalRequest)
def deduct_balance(sender, instance, created, **kwargs):
    if instance.paid and not created:  # Check if the instance is marked as paid and not created (updated)
        user = instance.user  # Assuming each withdrawal request belongs to a user
        user.Balance -= instance.amount
        user.save()
