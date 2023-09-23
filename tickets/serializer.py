from rest_framework import serializers
from tickets.models import Ticket,  TicketsOrder



class TicketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=127)
    cpf = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=127) 
    added_by = serializers.CharField(source="user.email", read_only=True)
    added_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)


class TicketsOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    code = serializers.CharField(max_length=127)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_name(self, obj: TicketsOrder):
        return obj.ticket.code

    def get_buyed_by(self, obj: TicketsOrder):
        return obj.user.email

    def create(self, validated_data: dict) -> TicketsOrder:
        return TicketsOrder.objects.create(**validated_data)
