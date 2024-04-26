from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_password_changed_email(sender, instance, created, **kwargs):
    if not created and instance.has_changed('password'):
        template = render_to_string('password_changed_email_template.html', {'user': instance})
        subject = 'Your password has been changed'
        message = template
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)