from django.views.generic import CreateView

from .models import ContactBase
from .forms import ContactBaseForm
# if using without celery:
# from .service import send_email
from .tasks import send_some_email


class ContactBaseView(CreateView):
    """
    Create subscription form

    """
    model = ContactBase
    form_class = ContactBaseForm
    success_url = "/"
    template_name = "mail/subscribe.html"

    def form_valid(self, form):
        form.save()
        # if using without celery:
        # send_email(form.instance.email)
        send_some_email.delay(form.instance.email)
        return super().form_valid(form)
