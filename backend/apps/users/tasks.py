from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template import loader


@shared_task()
def send_mail_async(subject_template_name, email_template_name,
                    context, from_email, to_email,
                    email_type=None, html_email_template_name=None, attachments=None):
    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    # txt body
    body = loader.render_to_string(email_template_name, context)

    if not isinstance(to_email, list):
        to_email = [to_email]

    email_message = EmailMultiAlternatives(subject, body, from_email, to_email)

    if attachments:
        for attachment in attachments:
            email_message.attach(*attachment)

    if html_email_template_name is not None:
        html_email = loader.render_to_string(html_email_template_name,
                                             context)
        email_message.attach_alternative(html_email, 'text/html')

    email_message.send()
    return f"Send Email to {to_email} for {email_type}"
