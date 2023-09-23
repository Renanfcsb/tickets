from rest_framework.views import APIView, Request, Response, status
from tickets.models import Ticket,TicketsOrder
from tickets.serializer import TicketSerializer, TicketsOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from tickets.permissions import IsEmployeeOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TicketView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request) -> Response:
        tickets = Ticket.objects.all()
        result_page = self.paginate_queryset(tickets, request)
        serializer = TicketSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = TicketSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TicketDatailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request, ticket_id: int) -> Response:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = TicketSerializer(ticket)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, ticket_id) -> Response:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, ticket_id) -> Response:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        seriliazer = TicketsOrderSerializer(data=request.data)
        seriliazer.is_valid(raise_exception=True)

        seriliazer.save(ticket=ticket, user=request.user)

        return Response(seriliazer.data, status.HTTP_201_CREATED)
