from django.urls import path
from tickets.views import TicketView, TicketDatailView, TicketOrderView


urlpatterns = [
    path("tickets/", TicketView.as_view()),
    path("tickets/<int:ticket_id>/", TicketDatailView.as_view()),
    path("tickets/<int:ticket_id>/orders/", TicketOrderView.as_view()),
]
