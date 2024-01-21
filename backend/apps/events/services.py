from django.contrib.auth import get_user_model
from django.conf import settings

from apps.users.tasks import send_mail_async
from .models import Event

User = get_user_model()


def register_to_event(user: User, event: Event) -> None:
    event.participants.add(user)

    context = {
        'user_full_name': user.full_name,
        'event_title': event.title
    }
    send_mail_async.delay(
        subject_template_name='events/email/event_registration_success_subject.txt',
        html_email_template_name='events/email/event_registration_success_message.html',
        email_template_name='events/email/event_registration_success_message.txt',
        context=context,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_email=user.email,
        email_type='event_registration',
    )
