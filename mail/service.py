from django.core.mail import send_mail


def send_email(mail):
    """
    Sending test email

    """
    send_mail(
        "Now you've subscribed!",
        "That's great!",
        "settings.EMAIL_HOST_USER",
        [mail],
        fail_silently=False
    )
