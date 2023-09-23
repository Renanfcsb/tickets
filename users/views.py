from rest_framework.views import APIView, Request, Response, status
from users.models import User
from .serializer import UserRegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserRegisterSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserRegisterSerializer(user, request.data, partial=True)

        serializer.is_valid()

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
