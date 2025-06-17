from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import UserModel
from users.serializers import UserModelDetailSerializer


class UserMeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_serializer = UserModelDetailSerializer(request.user)
        return Response({"user": user_serializer.data}, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user_serializer = UserModelDetailSerializer(user)
        return Response({"user": user_serializer.data}, status=status.HTTP_200_OK)
