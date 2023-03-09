from django.urls import path

from .views import ContactBaseView

urlpatterns = [
    path('', ContactBaseView.as_view(), name="contact"),
]
