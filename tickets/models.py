from django.db import models
from users.models import User



class Ticket(models.Model):
    name = models.CharField(max_length=127)
    cpf = models.CharField(max_length=11)
    added_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=127)
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ticket"
    )
    orders = models.ManyToManyField(
        "users.User", through="tickets.TicketsOrder", related_name="ticket_order"
    )


class TicketsOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    code = models.CharField(max_length=127)
    ticket = models.ForeignKey(
        "tickets.Ticket", on_delete=models.CASCADE, related_name="order_ticket"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_ticket"
    )
