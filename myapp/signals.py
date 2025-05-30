from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=User)
def send_notification_on_user_create(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications',
            {
                'type': 'send_notification',
                'title': 'Yangi foydalanuvchi!',
                'message': f'{instance.username} ro‘yxatdan o‘tdi.'
            }
        )
