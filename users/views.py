from rest_framework.views import APIView
from users.serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.serializers import UserModelMeSerializer

class UserMeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_serializer = UserModelMeSerializer(request.user)

        return Response({"user": user_serializer.data}, status=status.HTTP_200_OK)
